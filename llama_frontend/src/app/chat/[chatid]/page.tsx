"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { postQuestion, getChat } from "@/components/api"
import { Textarea, Button } from "@material-tailwind/react";
import ReactMarkdown from 'react-markdown';


export default function Chat({ params }: { params: { chatid: number } }) {
  const router = useRouter();
  const [question, setQuestion] = useState("");
  const [questions, setQuestions] = useState([]);
  const [is_answered, setIsAnswered] = useState(false);
  const getQuestions = async () => {
    const { chatid } = await params
    let [questions_temp, is_answered_temp] = await getChat(chatid);
    setQuestions(questions_temp)
    setIsAnswered(is_answered_temp)
    console.log(is_answered)
  }
  
  useEffect(() => {
    const intervalId = setInterval(async () => {
      if (!is_answered) {
        console.log("Fetching data...");
        await getQuestions();
      } else {
        console.log("Question answered, stopping polling.");
        clearInterval(intervalId); // Stop polling when the condition is met
      }
    }, 1000); // 5-second interval
    return () => clearInterval(intervalId);
  }, [is_answered])

  const handleClick = async () => {
    if (question.length > 0) {
      const chatid = await postQuestion(question, params.chatid)
      window.location.reload();
    }
  }

  const handleHome = async () => {
    router.push(`/`);
  }

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <div className="relative w-[40rem]">
          {questions.map((question, index) => (
            <div key={index}>
              <p>Question:</p>
              <p>{question.question_text}</p>
              <p>Answer:</p>
              <ReactMarkdown>{question.answer_text}</ReactMarkdown>
              <br/>
            </div>
          ))}
        </div>
        <div className="relative w-[40rem]">
          <Textarea
            onChange={(e) => setQuestion(e.target.value)}
            value={question}
            label="Input your question"
            className="dark:text-white"
          />
          <div className="flex justify-between">
            <Button size="sm" className="rounded-md" placeholder={undefined} onClick={handleHome}>
              Home
            </Button>
            <Button size="sm" className="rounded-md" placeholder={undefined} onClick={handleClick}>
              Post Comment
            </Button>

          </div>
        </div>
      </main>
      <footer className="row-start-3 flex gap-6 flex-wrap items-center justify-center">
      </footer>
    </div>
  );
}
