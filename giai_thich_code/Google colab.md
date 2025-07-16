# Chat LangChain

GPT 4.1 Mini

Chat History

New chat

### Today

hướng dẫn dùng langchain trong google colab với openai,và ví dụ đơn giản

giải thích khái niệm LCEL trong langchain,cho ví dụ đơn giản dễ hiểu

Giải thích cho tôi: from langchain\_core.prompts import PromptTemplate

### Yesterday

Giải thích: from langchain\_core.prompts import PromptTemplate, FewShotPromptTemplate examples = \[ {"question": "How many DataCamp courses has Jack completed?", "answer": "36"}, {"question": "How much XP does Jack have on DataCamp?", "answer": "284,320XP"}, { "question": "What technology does Jack learn about most on DataCamp?", "answer": "Python", }, \] # Complete the prompt for formatting answers example\_prompt = PromptTemplate.from\_template("Question: {question}\\n{answer}") # Create the few-shot prompt prompt\_template = FewShotPromptTemplate( examples=examples, example\_prompt=example\_prompt, suffix="Question: {input}", input\_variables=\["input"\], ) prompt = prompt\_template.invoke( {"input": "What is Jack's favorite technology on DataCamp?"} ) print(prompt.text)

### Last 7 days

giải thích: prompt\_template = ChatPromptTemplate.from\_messages( \[ ("system", "You are a geography expert that returns the colors present in a country's flag."), ("human", "France"), ("ai", "blue, white, red"), ("human", "{country}") \] ) # Chain the prompt template and model, and invoke the chain llm\_chain = prompt\_template | llm country = "Japan" response = llm\_chain.invoke({"country": country}) print(response.content)

giải thích chi tiết tất cả list param và value của param của class HuggingFacePipeline

các tham số device trong function HuggingFacePipeline

New chatNew chat

hướng dẫn dùng langchain trong google colab với openai,và ví dụ đơn giản

Done

Research Plan & Sources

### Tìm hiểu cách cài đặt LangChain trong môi trường Google Colab.

* * *

Google Cloud SQL for SQL server | 🦜️🔗 LangChainGoogle Drive | 🦜️🔗 LangChainInstallation | 🦜️🛠️ LangSmithHow to install LangChain packages | 🦜️🔗 LangChainDocusaurus | 🦜️🔗 LangChainDocusaurus | 🦜️🔗 LangChainSee 2 more documents

### Tìm hiểu cách tích hợp LangChain với OpenAI API trong Google Colab.

* * *

OpenAI | 🦜️🔗 LangChainAzure OpenAI | 🦜️🔗 LangChainOpenLM | 🦜️🔗 LangChainJina Search | 🦜️🔗 LangChainxAI | 🦜️🔗 LangChainOpenAI | 🦜️🔗 LangChainSee 1 more documents

### Tìm một ví dụ đơn giản sử dụng LangChain với OpenAI trong Google Colab và giải thích chi tiết từng bước.

* * *

OpenAI | 🦜️🔗 LangChainOpenAI | 🦜️🔗 LangChainOpenLM | 🦜️🔗 LangChainAzure OpenAI | 🦜️🔗 LangChainIntroduction | 🦜️🔗 LangChainIntroduction | 🦜️🔗 LangChainSee 1 more documents

Selected Context

### Google Cloud SQL for SQL server | 🦜️🔗 LangChain

Google Cloud SQL for SQL server | 🦜️🔗 LangChain \[Skip to main content\](#\_\_docusaurus\_skipToContent\_fallback)\*\*Our Building Ambient Agents with LangGraph course is now available on LangChain Academy!\*\*\[\](https://colab.research.google.com/github/lan

### Google Drive | 🦜️🔗 LangChain

Google Drive | 🦜️🔗 LangChain \[Skip to main content\](#\_\_docusaurus\_skipToContent\_fallback)\*\*Our Building Ambient Agents with LangGraph course is now available on LangChain Academy!\*\*\[\](https://colab.research.google.com/github/langchain-ai/langchain

### Installation | 🦜️🛠️ LangSmith

Installation | 🦜️🛠️ LangSmith Skip to main contentOur Building Ambient Agents with LangGraph course is now available on LangChain Academy!API ReferenceRESTPythonJS/TSSearchRegionUSEUGo to AppGet StartedObservabilityEvaluationPrompt EngineeringDepl

Answer

Để sử dụng LangChain với OpenAI trong Google Colab, bạn có thể làm theo các bước sau đây cùng ví dụ đơn giản:

### 1\. Cài đặt thư viện cần thiết

Chạy lệnh sau trong Colab để cài đặt LangChain và gói tích hợp OpenAI:

pythonCopy

```python
!pip install --upgrade langchain langchain-openai
```

### 2\. Thiết lập API key của OpenAI

Bạn cần có API key của OpenAI. Nếu chưa có, đăng ký và lấy tại [https://platform.openai.com](https://platform.openai.com).

Sau đó, trong Colab, nhập API key và thiết lập biến môi trường:

pythonCopy

```python
import getpass
import os

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Nhập OpenAI API key của bạn: ")
```

### 3\. Ví dụ đơn giản sử dụng LangChain với OpenAI

Dưới đây là ví dụ tạo một mô hình ngôn ngữ đơn giản và gọi nó để trả lời câu hỏi:

pythonCopy

```python
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

# Khởi tạo mô hình OpenAI
llm = OpenAI()

# Tạo prompt template
prompt = PromptTemplate.from_template("Hãy dịch câu sau sang tiếng Đức: {input}")

# Tạo chain kết hợp prompt và mô hình
chain = prompt | llm

# Gọi chain với input
result = chain.invoke({"input": "I love programming."})

print(result)
```

Kết quả sẽ là câu dịch tiếng Đức của câu "I love programming." Ví dụ:

unknownCopy

```text
Ich liebe Programmieren.
```

* * *

Tóm lại, các bước chính là:

*   Cài đặt `langchain` và `langchain-openai`
*   Thiết lập biến môi trường `OPENAI_API_KEY`
*   Khởi tạo mô hình OpenAI trong LangChain
*   Tạo prompt và gọi chain để nhận kết quả

Bạn có thể mở rộng từ ví dụ này để xây dựng các ứng dụng phức tạp hơn với LangChain và OpenAI.

Tham khảo chi tiết hơn tại tài liệu chính thức LangChain: [https://python.langchain.com/docs/integrations/llms/openai/](https://python.langchain.com/docs/integrations/llms/openai/) \[${9}\]

* * *

dùng code mới nhất

Done

Research Plan & Sources

### Tìm hiểu cách sử dụng LangChain với OpenAI theo phiên bản mới nhất trong tài liệu chính thức, đặc biệt phần tích hợp OpenAI.

* * *

langchain\_openai 0.1.25 — 🦜🔗 LangChain 0.2.17OpenAI | 🦜️🔗 LangChainOpenAI | 🦜️🔗 LangChainlangchain\_nomic 0.1.2 — 🦜🔗 LangChain 0.2.17Azure OpenAI | 🦜️🔗 LangChainOpenLM | 🦜️🔗 LangChain

### Tìm ví dụ code mới nhất trong phần How-to guides hoặc Integration docs của LangChain để đảm bảo sử dụng API và cách khởi tạo đúng.

* * *

2Markdown | 🦜️🔗 LangChainDocusaurus | 🦜️🔗 LangChainDocusaurus | 🦜️🔗 LangChainHow-to Guides | 🦜️🔗 LangChainZoteroRetriever | 🦜️🔗 LangChainAgentQL | 🦜️🔗 LangChainSee 2 more documents

### Tổng hợp và viết lại ví dụ đơn giản chạy được trên Google Colab với phiên bản mới nhất của LangChain và OpenAI.

* * *

langchain\_nomic 0.1.2 — 🦜🔗 LangChain 0.2.17Docusaurus | 🦜️🔗 LangChainNLP Cloud | 🦜️🔗 LangChainJina Search | 🦜️🔗 LangChainOpenAI | 🦜️🔗 LangChainAzure OpenAI | 🦜️🔗 LangChainSee 4 more documents

Selected Context

### langchain\_openai 0.1.25 — 🦜🔗 LangChain 0.2.17

langchain\_openai 0.1.25 — 🦜🔗 LangChain 0.2.17 This is a legacy site. Please use the latest v0.2 and v0.3 API references instead. LangChain Core Community Experimental Text splitters ai21 airbyte anthropic astradb aws azure-dynamic-sessi

### OpenAI | 🦜️🔗 LangChain

OpenAI | 🦜️🔗 LangChain \[Skip to main content\](#\_\_docusaurus\_skipToContent\_fallback)\*\*Our Building Ambient Agents with LangGraph course is now available on LangChain Academy!\*\*\[\](https://colab.research.google.com/github/langchain-ai/langchain/blob/

### OpenAI | 🦜️🔗 LangChain

OpenAI | 🦜️🔗 LangChain \[Skip to main content\](#\_\_docusaurus\_skipToContent\_fallback)\*\*Our Building Ambient Agents with LangGraph course is now available on LangChain Academy!\*\*\[\](https://github.com/langchain-ai/langchain/blob/master/docs/docs/integ

Answer

Dưới đây là hướng dẫn sử dụng LangChain với OpenAI trong Google Colab theo cách mới nhất (dựa trên API hiện tại của LangChain và langchain-openai):

* * *

### 1\. Cài đặt thư viện

Chạy lệnh sau trong Colab để cài đặt:

pythonCopy

```python
!pip install --upgrade langchain langchain-openai
```

* * *

### 2\. Thiết lập API key OpenAI

Nhập API key và thiết lập biến môi trường:

pythonCopy

```python
import os
import getpass

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Nhập OpenAI API key của bạn: ")
```

* * *

### 3\. Ví dụ đơn giản sử dụng LangChain với OpenAI

pythonCopy

```python
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

# Khởi tạo mô hình OpenAI (mặc định dùng gpt-3.5-turbo)
llm = OpenAI()

# Tạo prompt template
prompt = PromptTemplate.from_template("Hãy dịch câu sau sang tiếng Đức: {input}")

# Tạo chain kết hợp prompt và mô hình
chain = prompt | llm

# Gọi chain với input
result = chain.invoke({"input": "I love programming."})

print(result)
```

* * *

### Giải thích

*   `OpenAI()` khởi tạo mô hình chat completion của OpenAI.
*   `PromptTemplate.from_template` tạo prompt có tham số `{input}`.
*   Dùng toán tử `|` để nối prompt và mô hình thành một chain.
*   `chain.invoke` truyền dữ liệu đầu vào và nhận kết quả trả về.

* * *

Bạn có thể thay đổi câu hỏi hoặc prompt để thử nghiệm các tác vụ khác nhau.

* * *

Tài liệu tham khảo chính thức LangChain OpenAI integration:  
[https://python.langchain.com/docs/integrations/llms/openai/](https://python.langchain.com/docs/integrations/llms/openai/) \[2\]\[{2}\]\[2\]\[{9}\]

* * *

from langchain\_openai import ChatOpenAI

Done

Research Plan & Sources

### Tìm hiểu cách sử dụng lớp ChatOpenAI trong thư viện langchain\_openai dựa trên tài liệu tích hợp OpenAI của LangChain.

* * *

WeChat | 🦜️🔗 LangChainChatOpenAI | 🦜️🔗 LangChainiMessage | 🦜️🔗 LangChainOpenAI | 🦜️🔗 LangChainOpenAI | 🦜️🔗 LangChainlangchain\_openai 0.1.25 — 🦜🔗 LangChain 0.2.17

### Tìm ví dụ đơn giản minh họa cách khởi tạo và sử dụng ChatOpenAI trong Google Colab với API key OpenAI.

* * *

ChatOpenAI | 🦜️🔗 LangChainOpenAI | 🦜️🔗 LangChainChat model tabs | 🦜🕸️LangGraphWeChat | 🦜️🔗 LangChainAzure OpenAI | 🦜️🔗 LangChain

### Tổng hợp hướng dẫn và ví dụ code mới nhất sử dụng ChatOpenAI trong Google Colab.

* * *

ChatOpenAI | 🦜️🔗 LangChainChat model tabs | 🦜🕸️LangGraphWeChat | 🦜️🔗 LangChainChatGoogleGenerativeAI | 🦜️🔗 LangChainChatOpenAI | 🦜️🔗 LangChainGoogle Books | 🦜️🔗 LangChain

Selected Context

### WeChat | 🦜️🔗 LangChain

\`\`\`python from langchain\_openai import ChatOpenAI llm = ChatOpenAI() for chunk in llm.stream(messages\[0\]\["messages"\]): print(chunk.content, end="", flush=True) \`\`\` \*\*API Reference:\*\*\[ChatOpenAI\](https://python.langchain.com/api\_reference/opena

### ChatOpenAI | 🦜️🔗 LangChain

ChatOpenAI | 🦜️🔗 LangChain \[Skip to main content\](#\_\_docusaurus\_skipToContent\_fallback)\*\*Our Building Ambient Agents with LangGraph course is now available on LangChain Academy!\*\*\[\](https://colab.research.google.com/github/langchain-ai/langchain/b

### iMessage | 🦜️🔗 LangChain

\*\*API Reference:\*\*\[map\_ai\_messages\](https://python.langchain.com/api\_reference/community/chat\_loaders/langchain\_community.chat\_loaders.utils.map\_ai\_messages.html) | \[merge\_chat\_runs\](https://python.langchain.com/api\_reference/community/chat\_loaders/l

Answer

`from langchain_openai import ChatOpenAI` là câu lệnh Python dùng để import lớp `ChatOpenAI` từ gói `langchain_openai`. Đây là lớp tích hợp mô hình chat của OpenAI trong LangChain, giúp bạn dễ dàng gọi các mô hình chat như GPT-4, GPT-3.5-turbo để tạo các cuộc hội thoại hoặc xử lý ngôn ngữ tự nhiên theo dạng chat.

### Cách sử dụng cơ bản với `ChatOpenAI` trong Google Colab

1.  **Cài đặt thư viện**

pythonCopy

```python
!pip install --upgrade langchain langchain-openai
```

2.  **Thiết lập API key**

pythonCopy

```python
import os
import getpass

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Nhập OpenAI API key của bạn: ")
```

3.  **Khởi tạo và gọi mô hình ChatOpenAI**

pythonCopy

```python
from langchain_openai import ChatOpenAI

# Khởi tạo mô hình chat OpenAI, ví dụ dùng GPT-4
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Tạo danh sách messages theo định dạng (role, content)
messages = [
    ("system", "Bạn là trợ lý giúp dịch tiếng Anh sang tiếng Pháp."),
    ("human", "I love programming."),
]

# Gọi mô hình để lấy phản hồi
ai_message = llm.invoke(messages)

print(ai_message.content)
```

Kết quả sẽ là câu dịch tiếng Pháp của câu "I love programming." Ví dụ:

unknownCopy

```text
J'adore la programmation.
```

* * *

### Tóm tắt

*   `ChatOpenAI` là lớp để tương tác với các mô hình chat của OpenAI trong LangChain.
*   Bạn truyền vào danh sách `messages` với vai trò như `system`, `human`, `assistant`.
*   Phương thức `invoke` trả về một đối tượng chứa nội dung phản hồi từ mô hình.

Bạn có thể tham khảo thêm tài liệu chính thức về `ChatOpenAI` tại:  
[https://python.langchain.com/api\_reference/openai/chat\_models/langchain\_openai.chat\_models.base.ChatOpenAI.html](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) \[1\]\[{1}\]\[1\]\[{2}\]

* * *

phân biệt class ChatOpenAI va class Openai

Done

Research Plan & Sources

### Tìm hiểu tài liệu chính thức của LangChain về lớp ChatOpenAI để hiểu chức năng và cách sử dụng.

* * *

langchain\_openai 0.1.25 — 🦜🔗 LangChain 0.2.17ChatOpenAI | 🦜️🔗 LangChainOpenAI | 🦜️🔗 LangChainOpenAI | 🦜️🔗 LangChainWeChat | 🦜️🔗 LangChain

### Tìm hiểu tài liệu chính thức của LangChain về lớp OpenAI để hiểu chức năng và cách sử dụng.

* * *

langchain\_openai 0.1.25 — 🦜🔗 LangChain 0.2.17OpenAI | 🦜️🔗 LangChainDocusaurus | 🦜️🔗 LangChainlangchain 0.2.17 — 🦜🔗 LangChain 0.2.17Azure OpenAI | 🦜️🔗 LangChainOpenAI | 🦜️🔗 LangChainSee 1 more documents

### So sánh hai lớp dựa trên mục đích, cách khởi tạo, phương thức chính và các trường hợp sử dụng điển hình.

* * *

Markdownify | 🦜️🔗 LangChainMarkdownify | 🦜️🔗 LangChainNimbleSearchRetriever | 🦜️🔗 LangChainDocumentation Style Guide | 🦜️🔗 LangChainComet | 🦜️🔗 LangChainPyPDFium2Loader | 🦜️🔗 LangChainSee 3 more documents

Selected Context

### langchain\_openai 0.1.25 — 🦜🔗 LangChain 0.2.17

langchain\_openai 0.1.25 — 🦜🔗 LangChain 0.2.17 This is a legacy site. Please use the latest v0.2 and v0.3 API references instead. LangChain Core Community Experimental Text splitters ai21 airbyte anthropic astradb aws azure-dynamic-sessi

### ChatOpenAI | 🦜️🔗 LangChain

ChatOpenAI | 🦜️🔗 LangChain \[Skip to main content\](#\_\_docusaurus\_skipToContent\_fallback)\*\*Our Building Ambient Agents with LangGraph course is now available on LangChain Academy!\*\*\[\](https://colab.research.google.com/github/langchain-ai/langchain/b

### OpenAI | 🦜️🔗 LangChain

OpenAI | 🦜️🔗 LangChain \[Skip to main content\](#\_\_docusaurus\_skipToContent\_fallback)\*\*Our Building Ambient Agents with LangGraph course is now available on LangChain Academy!\*\*\[\](https://colab.research.google.com/github/langchain-ai/langchain/blob/

Answer

Dưới đây là sự khác biệt chính giữa hai lớp `ChatOpenAI` và `OpenAI` trong LangChain:

* * *

### 1\. `ChatOpenAI`

*   **Mục đích:** Tích hợp các **mô hình chat completion** của OpenAI (ví dụ: GPT-4, GPT-3.5-turbo).
*   **Đặc điểm:**
    *   Thiết kế để xử lý các cuộc hội thoại theo định dạng message (danh sách các tin nhắn với vai trò như `system`, `human`, `assistant`).
    *   Hỗ trợ các tính năng chat nâng cao như tool calling, structured output, streaming token-level, xử lý input đa dạng (text, image, audio).
    *   Phù hợp cho các ứng dụng cần tương tác dạng hội thoại, agent, chatbot.
*   **Ví dụ sử dụng:**

pythonCopy

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0)

messages = [
    ("system", "Bạn là trợ lý dịch tiếng Anh sang tiếng Pháp."),
    ("human", "I love programming."),
]

response = llm.invoke(messages)
print(response.content)
```

*   **Tham khảo:** [https://python.langchain.com/api\_reference/openai/chat\_models/langchain\_openai.chat\_models.base.ChatOpenAI.html](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) \[1\]\[{1}\]\[1\]\[{2}\]

* * *

### 2\. `OpenAI`

*   **Mục đích:** Tích hợp các **mô hình text completion** truyền thống của OpenAI (ví dụ: GPT-3 text-davinci-003).
*   **Đặc điểm:**
    *   Là lớp cơ bản để gọi API completion theo kiểu prompt text đơn giản.
    *   Thường dùng cho các tác vụ tạo văn bản, trả lời câu hỏi, tóm tắt, không theo dạng hội thoại.
    *   Ít phù hợp cho các ứng dụng chat đa lượt hoặc cần quản lý trạng thái hội thoại.
*   **Ví dụ sử dụng:**

pythonCopy

```python
from langchain_openai import OpenAI

llm = OpenAI()

response = llm.invoke("Hello, how are you?")
print(response)
```

*   **Tham khảo:** [https://python.langchain.com/api\_reference/openai/llms/langchain\_openai.llms.base.OpenAI.html](https://python.langchain.com/api_reference/openai/llms/langchain_openai.llms.base.OpenAI.html) \[3\]\[{3}\]\[3\]\[{9}\]

* * *

### Tóm tắt so sánh

Đặc điểm

ChatOpenAI

OpenAI

Loại mô hình

Chat completion (GPT-4, GPT-3.5)

Text completion (GPT-3, Davinci)

Định dạng input

Danh sách messages (role, content)

Chuỗi prompt text đơn giản

Ứng dụng chính

Chatbot, agent, hội thoại đa lượt

Tạo văn bản, trả lời prompt đơn

Tính năng hỗ trợ

Streaming, tool calling, structured output

Tương đối đơn giản

* * *

Nếu bạn muốn xây dựng ứng dụng chat hoặc agent, nên dùng `ChatOpenAI`. Nếu chỉ cần gọi mô hình tạo văn bản đơn giản, `OpenAI` có thể đủ dùng.

Hy vọng giải thích này giúp bạn phân biệt rõ hai lớp này!

* * *

bổ sung config base\_url

Done

Research Plan & Sources

### Tìm hiểu cách cấu hình \`base\_url\` cho các lớp \`ChatOpenAI\` và \`OpenAI\` trong tài liệu LangChain, đặc biệt phần tích hợp OpenAI.

* * *

langchain\_openai 0.1.25 — 🦜🔗 LangChain 0.2.17ChatOpenAI | 🦜️🔗 LangChainChat model tabs | 🦜🕸️LangGraphOpenAI | 🦜️🔗 LangChainAzure OpenAI | 🦜️🔗 LangChainOpenAI | 🦜️🔗 LangChain

### Kiểm tra ví dụ hoặc phần hướng dẫn về cách truyền tham số \`base\_url\` khi khởi tạo các lớp này.

* * *

LangChain Python API Reference Documentation.langsmith.utils — 🦜️🛠️ LangSmith documentationURL | 🦜️🔗 LangChainBrowserbase | 🦜️🔗 LangChainWebBaseLoader | 🦜️🔗 LangChainSee 4 more documents

### Tổng hợp cách cấu hình \`base\_url\` trong code mẫu cho cả \`ChatOpenAI\` và \`OpenAI\`.

* * *

ChatOpenAI | 🦜️🔗 LangChainWeChat | 🦜️🔗 LangChainlangchain\_openai 0.1.25 — 🦜🔗 LangChain 0.2.17Chat model tabs | 🦜🕸️LangGraph

Selected Context

### langchain\_openai 0.1.25 — 🦜🔗 LangChain 0.2.17

langchain\_openai 0.1.25 — 🦜🔗 LangChain 0.2.17 This is a legacy site. Please use the latest v0.2 and v0.3 API references instead. LangChain Core Community Experimental Text splitters ai21 airbyte anthropic astradb aws azure-dynamic-sessi

### ChatOpenAI | 🦜️🔗 LangChain

ChatOpenAI | 🦜️🔗 LangChain \[Skip to main content\](#\_\_docusaurus\_skipToContent\_fallback)\*\*Our Building Ambient Agents with LangGraph course is now available on LangChain Academy!\*\*\[\](https://colab.research.google.com/github/langchain-ai/langchain/b

### Chat model tabs | 🦜🕸️LangGraph

Chat model tabs Chat model tabs OpenAIAnthropicAzureGoogle GeminiAWS Bedrock pip install -U "langchain\[openai\]" import os from langchain.chat\_models import init\_chat\_model os.environ\["OPENAI\_API\_KEY"\] = "sk-..." llm = init\_chat\_model("openai:gpt

Answer

Bạn có thể bổ sung cấu hình `base_url` khi khởi tạo các lớp `ChatOpenAI` hoặc `OpenAI` trong LangChain để chỉ định endpoint API tùy chỉnh (ví dụ khi dùng proxy hoặc dịch vụ OpenAI không mặc định).

### Ví dụ với `ChatOpenAI`:

pythonCopy

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    base_url="https://api.openai.com/v1"  # Thay bằng URL API tùy chỉnh nếu cần
)

messages = [
    ("system", "Bạn là trợ lý dịch tiếng Anh sang tiếng Pháp."),
    ("human", "I love programming."),
]

response = llm.invoke(messages)
print(response.content)
```

### Ví dụ với `OpenAI`:

pythonCopy

```python
from langchain_openai import OpenAI

llm = OpenAI(
    base_url="https://api.openai.com/v1"  # URL API tùy chỉnh
)

response = llm.invoke("Hello, how are you?")
print(response)
```

* * *

### Lưu ý

*   `base_url` mặc định là endpoint OpenAI chính thức, bạn chỉ cần cấu hình khi dùng dịch vụ proxy hoặc môi trường đặc biệt.
*   Ngoài `base_url`, bạn có thể cấu hình thêm `api_key`, `organization`, `timeout`, `max_retries`... khi khởi tạo.

* * *

Tham khảo thêm trong tài liệu API LangChain OpenAI integration:  
[https://python.langchain.com/api\_reference/openai/chat\_models/langchain\_openai.chat\_models.base.ChatOpenAI.html](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)  
[https://python.langchain.com/api\_reference/openai/llms/langchain\_openai.llms.base.OpenAI.html](https://python.langchain.com/api_reference/openai/llms/langchain_openai.llms.base.OpenAI.html) \[1\]\[{1}\]\[1\]\[{3}\]

Scroll to bottom

Send