from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv(override=True)

llm=ChatGroq(model="openai/gpt-oss-120b",
             max_tokens=5000,temperature=0.6)

prompt_template=PromptTemplate.from_template(""" Analyze given {topic} and provide respopnse in only three lines """)

prompt=prompt_template.invoke(
                            {"topic":input("Enter topic - ")}
)

response=llm.invoke(prompt)
print(response.content)
