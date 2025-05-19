"use client";

import { useState } from "react";
import { notFound, useRouter, useSearchParams } from "next/navigation";
import { postQuestion } from "@/components/api"
import { Textarea, Button } from "@material-tailwind/react";


export default function Home() {
  const router = useRouter();
  const [question, setQuestion] = useState("");
  const handleClick = async () => {
    if (question.length > 0) {
      const chatid = await postQuestion(question, null)
      router.push(`/chat/${chatid}`);
    }
  }

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <div className="relative w-[32rem]">
          <Textarea
            onChange={(e) => setQuestion(e.target.value)}
            value={question}
            label="Input your question"
            className="dark:text-white"
          />
          <div className="flex justify-end">
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
