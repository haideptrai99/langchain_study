import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# --- Cấu hình biến môi trường ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

# Tắt LangSmith tracing để tránh cảnh báo
LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING")
LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")


if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

# --- Khởi tạo LLM ---
llm = ChatOpenAI(
    model=OPENAI_MODEL,
    temperature=0.0,
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_API_BASE,
)

# --- Khởi tạo công cụ (Tools) ---
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=2000)
wikipedia_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)
tools = [wikipedia_tool]

# --- Khởi tạo Agent ---
prompt = hub.pull("hwchase17/react")
agent_runnable = create_react_agent(llm, tools, prompt)
# Đặt verbose=False để không hiển thị quá trình suy luận
agent = AgentExecutor(
    agent=agent_runnable, tools=tools, verbose=False, handle_parsing_errors=True
)

# --- Thực thi Agent và lấy kết quả cuối cùng ---
try:
    response = agent.invoke(
        {"input": "How many people live in NewYork City?", "chat_history": []}
    )
    # Chỉ in ra giá trị của khóa 'output'
    print(response.get("output"))
except Exception as e:
    print(f"An error occurred during agent invocation: {e}")
