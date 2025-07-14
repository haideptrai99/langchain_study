# Import the class for defining Hugging Face pipelines
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

# Define the LLM from the Hugging Face model ID
llm = HuggingFacePipeline.from_model_id(
    model_id="crumb/nano-mistral",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 20},
)

template = "Thời tiết hôm nay ở {city} như thế nào?"
prompt_template = PromptTemplate.from_template(template=template)
# prompt = prompt_template.invoke({"city": "Bình Dương"})
# print(prompt)
llm_chain = prompt_template | llm
response = llm_chain.invoke({"city": "Bình Dương"})
print(response)
