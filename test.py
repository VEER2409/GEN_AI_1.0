from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage,HumanMessage
from dotenv import load_dotenv
load_dotenv(override=True)

llm=ChatGroq(model="openai/gpt-oss-120b",max_tokens=100)
history=[]

print("My first chatbot")
while True:
    prompt=input("user: ")
    history.append(HumanMessage(content=prompt))
    if prompt=="exit":
        break
    response=llm.invoke(history)
    history.append(AIMessage(content=response.content))
    print(response.content)

print(history)