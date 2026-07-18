from dotenv import load_dotenv
from groq import Groq
from flaskblog.assistant.prompts import SYSTEM_PROMPT
import os

load_dotenv()

client = Groq(
    api_key="",
)


def ask_ai(user_message):

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": user_message
            }

        ]

    )

    return response.choices[0].message.content


