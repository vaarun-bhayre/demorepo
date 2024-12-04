import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()
promt =input("enter a question")

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": promt,

        }
    ],
    model="llama3-70b-8192",
)

print(chat_completion.choices[0].message.content)