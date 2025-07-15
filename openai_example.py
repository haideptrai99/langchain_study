import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
llm = ChatOpenAI(
    model="openai:gpt-4o-mini",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.7,
    base_url=OPENAI_API_BASE,
)
template = "Thời tiết hôm nay ở {city} như thế nào?"
prompt_template = PromptTemplate.from_template(template=template)
# prompt = prompt_template.invoke({"city": "Bình Dương"})
# print(prompt)
llm_chain = prompt_template | llm
response = llm_chain.invoke({"city": "Bình Dương"})
print(response.content)
