from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage,HumanMessage

load_dotenv(override=True)

llm=ChatGroq(model="openai/gpt-oss-120b")

messages=[]

chat_prompt=ChatPromptTemplate.from_messages( [
                                ("system","You are a funny AI assistant "),
                                ("placeholder","{history}"),
                                ("human","{question}")
                                ] )

while True:

    prompt=input("Enetr your prompt - ")

    if prompt.lower()=="exit":
        break

    formatted_messages=chat_prompt.invoke({"history":messages,"question":prompt})

    response=llm.invoke(formatted_messages)

    print("AI response - ",response.content)

    messages.append(HumanMessage(content=prompt))
    messages.append(AIMessage(content=response.content))
