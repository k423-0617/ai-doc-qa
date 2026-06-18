# AI 文档问答系统

基于 DeepSeek API 的文档问答程序，支持上传文档并根据内容回答问题。

## 功能

- 支持读取 TXT 格式文档
- 基于文档内容智能回答问题
- 支持切换不同文档
- 支持多轮问答

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/k423-0617/ai-doc-qa.git
cd ai-doc-qa
```

### 2. 安装依赖

```bash
pip install requests
```

### 3. 配置密钥

打开 `doc_qa.py`，找到第 12 行：

```python
API_KEY = "your-api-key-here"
```

替换成你的 DeepSeek API 密钥。

### 4. 运行

```bash
python doc_qa.py
```

## 使用示例

```
==================================================
  AI 文档问答系统 (Powered by DeepSeek)
==================================================

请输入文档路径: C:\文档\报告.txt

文档读取成功！（5000 字符）
--------------------------------------------------

请输入问题: 这篇报告的主要结论是什么？
AI: 根据文档内容，主要结论是...

请输入问题: 换文档
请输入新文档路径: C:\文档\另一篇.txt
新文档读取成功！

请输入问题: 退出
再见！
```

## 项目结构

```
ai-doc-qa/
├── doc_qa.py    # 主程序
├── README.md    # 项目说明
└── .gitignore   # Git忽略文件
```

## 技术栈

- Python 3
- DeepSeek API（OpenAI 兼容格式）
- requests 库

## 注意事项

- 目前支持 TXT 格式文档
- 文档内容过长时会自动截取前 3000 字符
- 需要有效的 DeepSeek API 密钥
