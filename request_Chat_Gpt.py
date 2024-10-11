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


"""
openai.api_key = os.getenv("CHAT_API_KEY")

def answer(message, list_of_messages=[]):
    list_of_messages.append(
        {"role": "user", "content": message}
    )

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=list_of_messages,
    )

    return response["choises"][0]["message"]


print(answer("Hello"))











# Carregar as variáveis de ambiente
load_dotenv()
OPENAI_API_KEY = os.getenv("CHAT_GPT_KEY")

# Configurar o modelo
modelo = ChatOpenAI(model="gpt-4o-mini")

# Configurar a memória de conversação
memoria = ConversationBufferMemory()

# Criar o template de mensagens do sistema e do usuário corretamente
template_messages = ChatPromptTemplate.from_messages([
    SystemMessage(content="Você é uma inteligência artificial de viagens. Responda a próxima questão considerando o contexto anterior."),
    HumanMessage(content="{informação}")
])

# Função para gerar a resposta com contexto
def answer(request):
    # Criar o prompt a partir do template
    print("helklo")
    print (request)
    prompt = template_messages.format_messages(informação=request)  # Retorna a lista de mensagens formatadas

    # Passar o histórico de mensagens e o prompt atual para o modelo
    response = modelo(messages=memoria.chat_memory.messages + prompt)

    # Armazenar a nova interação na memória
    memoria.save_context({"informação": request}, {"resposta": response.content})

    return response.content

# Exemplo de como usar
pergunta_1 = "Qual a capital de Portugal?"
print(answer(pergunta_1))  # Resposta: Lisboa

pergunta_2 = "Qual a comida mais famosa desse país?"
print(answer(pergunta_2))  # Resposta: Lisboa (contexto mantido)
"""
