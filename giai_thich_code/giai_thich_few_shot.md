Đoạn code này minh họa cách sử dụng Few-Shot Prompting trong LangChain để hướng dẫn mô hình ngôn ngữ trả lời câu hỏi dựa trên các ví dụ được cung cấp trước. Hãy phân tích chi tiết từng phần:

1.  Import thư viện:

pythonCopy

```python
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
```

*   Import các lớp cần thiết để tạo prompt template

2.  Định nghĩa các ví dụ:

pythonCopy

```python
examples = [
    {"question": "How many DataCamp courses has Jack completed?", "answer": "36"},
    {"question": "How much XP does Jack have on DataCamp?", "answer": "284,320XP"},
    {
        "question": "What technology does Jack learn about most on DataCamp?", 
        "answer": "Python",
    },
]
```

*   Tạo một danh sách các ví dụ về Jack và DataCamp
*   Mỗi ví dụ là một từ điển với hai khóa: `question` và `answer`

3.  Tạo prompt template cho các ví dụ:

pythonCopy

```python
example_prompt = PromptTemplate.from_template("Question: {question}\n{answer}")
```

*   Định dạng cách các ví dụ sẽ được hiển thị
*   Sử dụng `{question}` và `{answer}` để điền thông tin

4.  Tạo Few-Shot Prompt Template:

pythonCopy

```python
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)
```

*   `examples`: Danh sách các ví dụ đã định nghĩa
*   `example_prompt`: Cách định dạng các ví dụ
*   `suffix`: Mẫu cho câu hỏi mới
*   `input_variables`: Các biến đầu vào

5.  Tạo và in prompt:

pythonCopy

```python
prompt = prompt_template.invoke(
    {"input": "What is Jack's favorite technology on DataCamp?"}
)
print(prompt.text)
```

*   Gọi prompt template với câu hỏi mới
*   In ra văn bản prompt được tạo

Kết quả sẽ là một prompt bao gồm:

*   Các ví dụ ban đầu về Jack và DataCamp
*   Câu hỏi mới về công nghệ yêu thích của Jack

Mục đích của Few-Shot Prompting là cung cấp cho mô hình ngôn ngữ các ví dụ để hướng dẫn cách trả lời, giúp mô hình hiểu rõ hơn về nhiệm vụ và phong cách trả lời mong muốn.

Ưu điểm:

*   Giúp mô hình hiểu rõ hơn về nhiệm vụ
*   Cung cấp ngữ cảnh và ví dụ cụ thể
*   Dễ dàng điều chỉnh và mở rộng

Nhược điểm:

*   Số lượng ví dụ hạn chế
*   Chất lượng phụ thuộc nhiều vào các ví dụ được chọn

Good responseBad response

Scroll to bottom

Send