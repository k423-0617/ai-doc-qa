# -*- coding: utf-8 -*-
"""
AI 文档问答系统
上传文档，基于文档内容回答问题
"""

import os
import requests
import json

# ============ 配置文件路径 ============
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

def load_config():
    """加载配置，如果没有则提示用户输入"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)

    # 第一次运行，询问密钥
    print("=" * 50)
    print("  首次运行，请配置 DeepSeek API 密钥")
    print("  密钥获取地址：https://platform.deepseek.com/api_keys")
    print("=" * 50)
    api_key = input("\n请输入你的 DeepSeek API 密钥: ").strip()

    config = {"api_key": api_key}
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

    print("密钥已保存！下次运行无需重新输入。\n")
    return config

# ============ 加载配置 ============
config = load_config()
API_KEY = config["api_key"]
BASE_URL = "https://api.deepseek.com/v1/chat/completions"
MODEL = "deepseek-chat"

def read_file(file_path):
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='gbk') as f:
                return f.read()
        except:
            return None
    except Exception as e:
        print(f"读取文件出错: {e}")
        return None

def ask_ai(document, question):
    """基于文档内容回答问题"""
    prompt = f"""请基于以下文档内容回答用户的问题。如果文档中没有相关信息，请明确说明。

文档内容：
{document[:3000]}

用户问题：{question}"""

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "你是一个文档分析助手，根据提供的文档内容回答问题。回答要准确、简洁。"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 2000
    }

    try:
        response = requests.post(BASE_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"请求出错: {e}"
    except (KeyError, IndexError) as e:
        return f"解析响应出错: {e}"

def main():
    """主函数"""
    print("=" * 50)
    print("  AI 文档问答系统 (Powered by DeepSeek)")
    print("=" * 50)
    print()

    # 获取文件路径
    while True:
        file_path = input("请输入文档路径（或拖拽文件到此处）: ").strip()
        file_path = file_path.strip('"')

        if not file_path:
            continue

        if file_path in ["退出", "exit", "quit", "q"]:
            print("再见！")
            return

        if os.path.exists(file_path):
            break
        else:
            print(f"文件不存在: {file_path}\n")

    # 读取文档
    print(f"\n正在读取文档...")
    document = read_file(file_path)

    if document is None:
        print("无法读取文档，请检查文件格式。")
        return

    print(f"文档读取成功！（{len(document)} 字符）")
    print("-" * 50)

    # 问答循环
    while True:
        question = input("\n请输入问题（输入'换文档'切换文件，输入'退出'结束）: ").strip()

        if not question:
            continue

        if question in ["退出", "exit", "quit", "q"]:
            print("\n再见！")
            break

        if question in ["换文档", "change"]:
            new_path = input("请输入新文档路径: ").strip().strip('"')
            if os.path.exists(new_path):
                document = read_file(new_path)
                if document:
                    print(f"新文档读取成功！（{len(document)} 字符）")
                else:
                    print("无法读取该文档。")
            else:
                print("文件不存在。")
            continue

        print("\nAI: ", end="", flush=True)
        answer = ask_ai(document, question)
        print(answer)

if __name__ == "__main__":
    main()
