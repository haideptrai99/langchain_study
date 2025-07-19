import os
from langchain_openai import ChatOpenAI

# Import cần thiết cho Agents và Tools
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
llm = ChatOpenAI(
    model="openai:gpt-4o-mini",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.7,
    base_url=OPENAI_API_BASE,
)

# --- Định nghĩa Tool (Công cụ) ---
search_tool = DuckDuckGoSearchRun(name="DuckDuckGo Search")
tools = [search_tool]

# --- Sửa lỗi tại đây: Tạo Prompt cho Agent bằng cách sử dụng prompt ReAct tiêu chuẩn ---
# LangChain có một prompt template được thiết kế riêng cho ReAct Agent
# Prompt này sẽ tự động inject `tools`, `tool_names`, và `agent_scratchpad`
prompt_template = ChatPromptTemplate.from_template("""
Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
""")

# --- Tạo Agent ---
agent = create_react_agent(llm, tools, prompt_template)

# --- Tạo Agent Executor ---
# verbose=True:
# Cực kỳ hữu ích để gỡ lỗi và hiểu cách agent suy luận.
# Nó sẽ in ra các bước mà agent thực hiện (Observations, Thoughts, Actions).

# handle_parsing_errors=True:
# Giúp agent phục hồi nếu có lỗi phân tích cú pháp trong quá trình suy luận.
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)

# --- Invoke Agent để lấy thông tin thời tiết ---
question = "Thời tiết hôm nay ở Bình Dương như thế nào?"
print(f"Hỏi: {question}")
response = agent_executor.invoke({"input": question})

print("\n--- Phản hồi từ Agent ---")
print(response["output"])
