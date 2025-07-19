import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub

# Cập nhật đường dẫn import cho WikipediaTool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import (
    WikipediaAPIWrapper,
)  # Cần thêm cái này để cấu hình WikipediaTool

# --- Cấu hình biến môi trường ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
LANGCHAIN_TRACING_V2 = "false"
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set.")
# OPENAI_API_BASE có thể không cần thiết nếu bạn dùng API OpenAI trực tiếp
if not OPENAI_API_BASE:
    print(
        "Warning: OPENAI_API_BASE environment variable not set. Using default OpenAI API base URL."
    )

# --- Khởi tạo LLM ---
print("Initializing ChatOpenAI model...")
llm = ChatOpenAI(
    model="openai:gpt-4o-mini",
    temperature=0.0,
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_API_BASE,
)
print("ChatOpenAI model initialized.")

# --- Khởi tạo công cụ (Tools) ---
print("Initializing tools...")
# Khởi tạo API wrapper cho Wikipedia
# top_k_results (số lượng kết quả hàng đầu)
# doc_content_chars_max (số ký tự tối đa của nội dung tài liệu).
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=2000)
# Sử dụng WikipediaQueryRun thay vì WikipediaTool và truyền wrapper vào
wikipedia_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)
tools = [wikipedia_tool]
print(f"Tools initialized: {[tool.name for tool in tools]}")

# --- Khởi tạo Agent ---
print("Fetching agent prompt from LangChain Hub...")
prompt = hub.pull("hwchase17/react")
print("Agent prompt fetched.")

print("Creating ReAct agent...")
agent_runnable = create_react_agent(llm, tools, prompt)
# verbose=True:
# Cực kỳ hữu ích để gỡ lỗi và hiểu cách agent suy luận.
# Nó sẽ in ra các bước mà agent thực hiện (Observations, Thoughts, Actions).

# handle_parsing_errors=True:
# Giúp agent phục hồi nếu có lỗi phân tích cú pháp trong quá trình suy luận.
agent = AgentExecutor(
    agent=agent_runnable, tools=tools, verbose=True, handle_parsing_errors=True
)
print("ReAct agent created.")

# --- Thực thi Agent ---
print("\nInvoking agent with query: 'How many people live in New York City?'")
try:
    response = agent.invoke(
        {"input": "How many people live in New York City?", "chat_history": []}
    )
    print("\n--- Agent Response ---")
    print(response.get("output", response))
except Exception as e:
    print(f"An error occurred during agent invocation: {e}")
