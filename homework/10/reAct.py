import wikipediaapi
import os
from groq import Groq

with open('prompt.txt', 'r', encoding='utf-8') as f:
    prompt = f.read()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)
wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')

wiki_ans=""
content = ""
question = ""

while 1:
    content = prompt
    
    if wiki_ans:
        content += wiki_ans + question
    else:
        question = input("請輸入問題：")
        content += question
    #print(f"content:{content}")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="llama3-8b-8192",
    )
    respons=chat_completion.choices[0].message.content
    wiki_ans, content = "", ""
    if respons.find("call_wiki:") != -1:
        print(f"FIND:{respons[respons.find("call_wiki:")+10:].split()[0]}")
        page_py = wiki_wiki.page(respons[respons.find("call_wiki:")+10:].split()[0])
        wiki_ans = page_py.title + page_py.summary + page_py.text
        print("WIKI:" + page_py.title + page_py.summary[:60])
    print("RESPONS: ",chat_completion.choices[0].message.content)
    print("-"*50)