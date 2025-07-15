import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Define the LLM from the Hugging Face model ID
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
llm = ChatOpenAI(
    model="openai:gpt-4o-mini",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.0,
    base_url=OPENAI_API_BASE,
)
# Create a chat prompt template

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a calculator that responds with math,only respond with math,not use natural language.",
        ),
        ("human", "Answer this math question: What is two plus two?"),
        ("ai", "2+2=4"),
        ("human", "Answer this math question: {math}"),
    ]
)

# Chain the prompt template and model, and invoke the chain
llm_chain = prompt_template | llm
math = "What is two times five?"
response = llm_chain.invoke({"math": math})
print(response.content)  # Output: "2*5=10" for the math question
