'use client'

export async function postQuestion(question_text:string, chatid: null|number): Promise<number> {
  const apiUrl = 'http://localhost:3000/api/questions/'

  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
          "question_text": question_text,
          "is_answered": false,
          "is_corrected": false,
          "chat": chatid
        })
    })

    if (response.ok) {
      const responseData = await response.json()
      console.log(responseData)
      const chatid = responseData.chat_id
      return chatid
    } else {
      console.error('Error fetching data:', response.statusText)
      return 0
    }
  } catch (error) {
    console.error('Error fetching data:', error)
    return 0
  }
}


export async function getChat(chatid:number): Promise<[object, boolean]> {
  const apiUrl = `http://localhost:3000//api/chats/${chatid}/`

  try {
    const response = await fetch(apiUrl, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })

    if (response.ok) {
      const responseData = await response.json()
      console.log(responseData)
      let question_list = [];
      let is_answered = true
      for (let i = 0; i < responseData.questions.length; i++) {
        let question = responseData.questions[i]
        question_list.push({
          question_text : question.question_text,
          answer_text : question.answers[0].answer_text
        })
        is_answered = question.is_answered
      }
      return [question_list, is_answered]
    } else {
      console.error('Error fetching data:', response.statusText)
      return [[""], false]
    }
  } catch (error) {
    console.error('Error fetching data:', error)
    return [[""], false]
  }
}
