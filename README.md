# AI 文档问答系统

基于 DeepSeek API 的文档问答程序，支持上传文档并根据内容回答问题。

## 功能

- 支持多种文档格式：TXT、DOCX、PDF、CSV、XLSX、MD、HTML
- 基于文档内容智能回答问题
- 支持切换不同文档
- 支持多轮问答

## 前置条件

在使用本程序前，你需要：

1. **安装 Python 3**
   - 下载地址：https://www.python.org/downloads/
   - 安装时勾选 "Add Python to PATH"

2. **获取 DeepSeek API 密钥**
   - 注册地址：https://platform.deepseek.com
   - 注册后进入"API 密钥"页面，创建一个新密钥
   - 复制密钥（格式类似：sk-xxxxxxxxxxxxxxxx）

## 安装步骤

### 第一步：下载代码

打开命令行（Windows 按 Win+R 输入 cmd 回车），输入：

```
git clone https://github.com/k423-0617/ai-doc-qa.git
cd ai-doc-qa
```

如果没有 git 命令，可以直接在 GitHub 页面点击绿色的 "Code" 按钮，选 "Download ZIP"，解压后进入文件夹。

### 第二步：安装依赖

在命令行中输入以下任意一个（哪个能用就用哪个）：

```
pip install requests python-docx pdfplumber openpyxl
```

或者：

```
py -3 -m pip install requests python-docx pdfplumber openpyxl
```

或者：

```
python -m pip install requests python-docx pdfplumber openpyxl
```

### 第三步：运行程序

```
py -3 doc_qa.py
```

或者：

```
python doc_qa.py
```

首次运行时，程序会提示你输入 DeepSeek API 密钥。输入后会自动保存，下次无需重新输入。

## 支持的文件格式

| 格式 | 说明 | 需要安装的库 |
|------|------|-------------|
| TXT | 纯文本文件 | 无 |
| DOCX | Word 文档 | python-docx |
| PDF | PDF 文档 | pdfplumber |
| CSV | 逗号分隔值文件 | 无（Python内置） |
| XLSX | Excel 表格 | openpyxl |
| MD | Markdown 文件 | 无 |
| HTML | 网页文件 | 无（Python内置） |

## 使用方法

1. 运行程序后，输入文档路径（可以直接把文件拖拽到命令行窗口）
2. 程序会读取文档内容
3. 输入你想问的问题，AI 会根据文档内容回答
4. 输入"换文档"可以切换到其他文档
5. 输入"退出"结束程序

## 使用示例

```
==================================================
  AI 文档问答系统 (Powered by DeepSeek)
  支持格式：TXT、DOCX、PDF、CSV、XLSX、MD、HTML
==================================================

请输入文档路径: C:\Users\用户名\Desktop\报告.pdf

文档读取成功！（5000 字符）
--------------------------------------------------

请输入问题: 这篇报告的主要结论是什么？
AI: 根据文档内容，主要结论是...

请输入问题: 换文档
请输入新文档路径: C:\Users\用户名\Desktop\数据.xlsx
新文档读取成功！

请输入问题: 退出
再见！
```

## 常见问题

**Q: 提示"pip 不是命令"怎么办？**
A: 试试 `py -3 -m pip install requests`，或者检查 Python 是否安装正确。

**Q: 提示"python 不是命令"怎么办？**
A: 需要安装 Python 并勾选 "Add Python to PATH"。

**Q: 提示"请求出错 401"怎么办？**
A: API 密钥无效或过期，请检查密钥是否正确。

**Q: 提示"读取PDF需要安装pdfplumber库"怎么办？**
A: 运行 `py -3 -m pip install pdfplumber` 安装库。

**Q: 提示"读取XLSX需要安装openpyxl库"怎么办？**
A: 运行 `py -3 -m pip install openpyxl` 安装库。

## 项目结构

```
ai-doc-qa/
├── doc_qa.py      # 主程序
├── config.json    # 配置文件（首次运行自动生成）
├── README.md      # 项目说明
└── .gitignore     # Git 忽略文件
```

## 技术栈

- Python 3
- DeepSeek API（OpenAI 兼容格式）
- requests 库
- python-docx 库（用于读取 DOCX 文件）
- pdfplumber 库（用于读取 PDF 文件）
- openpyxl 库（用于读取 XLSX 文件）
