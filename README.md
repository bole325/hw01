hw01/
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
├── README.md
└── prompt_log.md

## 2. 创建交互日志 prompt_log.md

```markdown
# AI 编程交互日志

## 会话1：初始需求描述

### 用户 Prompt
我需要创建一个简单的计算器Python程序，包含基本的加减乘除功能。程序应该：
1. 有良好的模块化结构
2. 包含错误处理
3. 有命令行交互界面
4. 需要编写单元测试

### AI 响应
我将创建一个结构化的计算器项目，包含核心逻辑和测试代码。首先创建 calculator.py 实现计算功能...

### 用户 Prompt
代码看起来不错，但除法功能需要考虑除数为0的情况

### AI 响应
好的，我会添加异常处理来处理除数为0的情况，并返回友好的错误信息。

---

## 会话2：处理 Bug

### 用户 Prompt
测试时发现，当输入非数字字符时程序会崩溃，需要添加输入验证

### AI 响应
发现了输入验证的bug。我会添加 try-except 块来处理无效输入，并在 calculator.py 中添加类型检查。

代码修改如下：
```python
def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("错误：请输入有效的数字！")