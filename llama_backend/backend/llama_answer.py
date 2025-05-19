import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
import os
import shutil
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    Settings,
    load_index_from_storage,
    get_response_synthesizer,
)
from llama_index.core import ChatPromptTemplate
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.llms.ollama import Ollama
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

file_dir = os.path.dirname(__file__)
data_dir = os.path.join(file_dir, "../data")
index_dir = os.path.join(file_dir, "../index")


# embed_model = HuggingFaceEmbedding(model_name="stsb-xlm-r-multilingual")
# llm_model = # "llama3.3:70b-instruct-q4_K_M"
prompt = (
    "ルールに従い、与えられたContextを必ず使用し、Queryに対して回答をしてください。\n"
    "# Rule\n"
    "  1. Answer in a language used in Query.\n"
    "# Context Information\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\n"
    "# Query:\n"
    "{query_str}\n"
    "# Answer: "
)
prompt = ChatPromptTemplate(message_templates=[
    ChatMessage(content=prompt, role=MessageRole.USER),
])


def make_response(question, answer):
    """
    llm = Ollama(
        model=llm_model,
        request_timeout=120.0,
        temperature=0
    )
    """
    llm = OpenAI(model="gpt-4o", temperature=0)
    question_text = question.question_text

    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(f"{data_dir}/imported", exist_ok=True)
    os.makedirs(index_dir, exist_ok=True)
    path_list = os.listdir(data_dir)
    path_list = [f"{data_dir}/{i}" for i in path_list if (
        "pdf" in i or
        "txt" in i or
        "doc" in i
    )]
    print(path_list)
    if len(path_list) > 0:
        documents = SimpleDirectoryReader(input_dir=data_dir).load_data()
        index = VectorStoreIndex.from_documents(
            documents
        )
        index.storage_context.persist(persist_dir=index_dir)
        for path in path_list:
            shutil.move(path, path.replace("/data", "/data/imported"))
    else:
        storage_context = StorageContext.from_defaults(persist_dir=index_dir)
        index = load_index_from_storage(storage_context)  # , embed_model=embed_model)

    Settings.llm = llm
    # Settings.embed_model = embed_model
    retriever = VectorIndexRetriever(
        index=index,
        similarity_top_k=5,
    )
    response_synthesizer = get_response_synthesizer(
        response_mode="simple_summarize",
        text_qa_template=prompt,
        streaming=True
    )
    query_engine = RetrieverQueryEngine.from_args(
        retriever=retriever,
        response_synthesizer=response_synthesizer
    )

    response = query_engine.query(
        question_text
    )

    text_to_add = ""
    n_text = 0
    for text in response.response_gen:
        text_to_add += text
        n_text += 1
        is_recorded = False
        if n_text == 5 :
            answer.answer_text = text_to_add
            answer.save()
            n_text = 0
            is_recorded = True

    if not is_recorded:
        answer.answer_text = text_to_add
        answer.save()
    print(text_to_add)
    return response
