import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Define the LLM from the Hugging Face model ID
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
llm = ChatOpenAI(
    model="openai:gpt-4o-mini",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.7,
    base_url=OPENAI_API_BASE,
)
# Create a chat prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a geography expert that returns the colors present in a country's flag.",
        ),
        ("human", "France"),
        ("ai", "blue, white, red"),
        ("human", "{country}"),
    ]
)

# Chain the prompt template and model, and invoke the chain
llm_chain = prompt_template | llm

country = "vietnam"
response = llm_chain.invoke({"country": country})
print(response.content)  # Output: "red, white" for Japan's flag colors
