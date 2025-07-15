from langchain_core.prompts import PromptTemplate

template = "Expain this concept simply and concisely: {concept}"
prompt_template = PromptTemplate.from_template(template=template)
prompt = prompt_template.invoke({"concept": "Prompting LLMs"})
print(prompt.text)

example_prompt = PromptTemplate.from_template("Question: {question}\n{answer}")
prompt = example_prompt.invoke(
    {"question": "What is the capital of Italy?", "answer": "Rome"}
)

print(prompt.text)
