

import os
import openai



def ask_open_ai(message):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    data = openai.Completion.create(
    model="text-davinci-003",
    prompt= f"You are building a NBA Q/A machine for NBA fans. Answer this question a fan asked '{message}' ",
    max_tokens=200 
    )
    answer = data["choices"][0]["text"]
    return answer

