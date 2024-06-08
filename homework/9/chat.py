
import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
while 1:
    content="""
    I want to practice English, use English to talk to me, and correct my grammar or vocabulary mistakes.
    """+input()
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="llama3-8b-8192",
    )

    print("Ans: ",chat_completion.choices[0].message.content)
    print("-"*50)