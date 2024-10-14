from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))


def answer(message, list_of_messages=[{"role": "system", "content": "You are a Chagpt to help people to Travel, just answer questions about travel. Your name is TourAi"}]):

    list_of_messages.append(
        {"role": "user", "content": message}
    ) 
    if len(list_of_messages) > 5:
        # Quero remover o segundo elemento
        list_of_messages.pop(1)
        list_of_messages.pop(1)

    chat_completion = client.chat.completions.create(
        messages=list_of_messages,
        model="gpt-3.5-turbo",
    )
    print("Total de tokens usados: ", chat_completion.usage.total_tokens)
    response = chat_completion.choices[0].message.content
    list_of_messages.append(
        {"role": "assistant", "content": response}
    )
    print(response)
    return response
