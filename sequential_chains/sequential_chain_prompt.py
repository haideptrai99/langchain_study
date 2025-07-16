from langchain_core.prompts import PromptTemplate

learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?",
)
time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="I only have one week. Can you create a plan to help me hit this goal: {learning_plan}",
)
print(learning_prompt.invoke({"activity": "play golf"}))
print(time_prompt.invoke({"learning_plan": "play golf every day for an hour"}))
# print(learning_prompt.invoke({"activity": "play golf"}))
# print(time_prompt.invoke({"learning_plan": "play golf every day for an hour"}))
learning_prompt_2 = PromptTemplate.from_template(
    "I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)
print(learning_prompt_2.invoke({"activity": "play golf"}))
