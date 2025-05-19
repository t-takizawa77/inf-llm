from background_task import background
from .models import Question, Answer
from .llama_answer import make_response


@background()
def process_question_data(question_id):
    print("processing question data")
    try:
        question = Question.objects.get(id=question_id)
        answer = Answer.objects.create(
            answer_text="...Thinking",
            question=question,
        )
        response = make_response(question, answer)
        question.is_answered = True
        question.save()
        print(f"Answer created: {response}")
    except Question.DoesNotExist:
        print(f"Question with id {question_id} not found")
