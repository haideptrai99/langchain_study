import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")
llm = ChatOpenAI(
    model=OPENAI_MODEL,
    openai_api_key=OPENAI_API_KEY,
    temperature=0,
    base_url=OPENAI_API_BASE,
)
template = "dịch từ {text} sang tiếng anh?"
prompt_template = PromptTemplate.from_template(template=template)
# prompt = prompt_template.invoke({"city": "Bình Dương"})
# print(prompt)
llm_chain = prompt_template | llm
response = llm_chain.invoke({"text": "Xin chào"})
print(response.content)
