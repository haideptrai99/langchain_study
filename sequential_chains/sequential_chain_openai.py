import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
llm = ChatOpenAI(
    model="openai:gpt-4o-mini",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.7,
    base_url=OPENAI_API_BASE,
)

learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?",
)
time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="I only have one week. Can you create a plan to help me hit this goal: {learning_plan}",
)
# Complete the sequential chain with LCEL
seq_chain = (
    {"learning_plan": learning_prompt | llm | StrOutputParser()}
    | time_prompt
    | llm
    | StrOutputParser()
)

# Call the chain
print(seq_chain.invoke({"activity": "play the harmonica"}))
