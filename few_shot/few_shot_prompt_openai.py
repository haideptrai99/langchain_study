from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
import os
from langchain_openai import ChatOpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
llm = ChatOpenAI(
    model="openai:gpt-4o-mini",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.7,
    base_url=OPENAI_API_BASE,
)
examples = [
    {"question": "How many DataCamp courses has Jack completed?", "answer": "36"},
    {"question": "How much XP does Jack have on DataCamp?", "answer": "284,320XP"},
    {
        "question": "What technology does Jack learn about most on DataCamp?",
        "answer": "Python",
    },
]

# Complete the prompt for formatting answers
example_prompt = PromptTemplate.from_template("Question: {question}\n{answer}")


# Create the few-shot prompt
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

prompt_response = prompt_template.invoke(
    {"input": "What is Jack's favorite technology on DataCamp?"}
)
print("-------List prompt-------")
print(prompt_response.text)
print("-------end list prompt-------")
print("\n")
print("-------LLM response-------")
llm_chain = prompt_template | llm
response = llm_chain.invoke(
    {"input": "What is Jack's favorite technology on DataCamp?"}
)
print(response.content)
print("-------end LLM response-------")
