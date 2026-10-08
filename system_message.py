from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv(override=True)

llm=ChatGroq(model="openai/gpt-oss-120b",temperature=0.1)
messages=[SystemMessage(content="You are funny  AI assistant,reply in funny way  ")]

print("My first chatbot")
while True:
    prompt=input("user: ")
    messages.append(HumanMessage(content=prompt))
    if prompt=="exit":
        break
    response=llm.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print(response.content)

print(messages)

