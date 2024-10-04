from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
OPENAI_API_KEY = os.getenv("CHAT_GPT_KEY")


modelo = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

template_messages = ChatPromptTemplate.from_messages([
    ("system", "És uma inteligência artificial de viagens, responde a próxima questão"),
    ("user", "{informação}"),
])

chain = template_messages | modelo | parser

def answer(request):
    response = chain.invoke({"informação":request})
    return response
#text = chain.invoke({"informação":"rio", "país":"França"})

#print(text)
