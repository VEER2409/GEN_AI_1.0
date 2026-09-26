from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv(override=True)

llm=ChatGroq(model="openai/gpt-oss-120b",temperature=1.0)

prompt=input("Enter prompt -")
response=llm.invoke(prompt)

print(response.content)