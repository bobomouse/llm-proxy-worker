# Claude API调用示例
# 使用代理访问Anthropic Claude API

import requests
import json

# 配置
PROXY_URL = "https://your-worker.workers.dev"  # 替换为您的Worker URL
API_KEY = "your-anthropic-api-key"  # 替换为您的Anthropic API密钥

# 构建请求
url = f"{PROXY_URL}/anthropic/v1/messages"
headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY,
    "anthropic-version": "2023-06-01"
}

payload = {
    "model": "claude-3-opus-20240229",
    "max_tokens": 500,
    "system": "你是一个友好、专业且乐于助人的AI助手。",
    "messages": [
        {
            "role": "user",
            "content": "解释一下人工智能中的'大型语言模型'是什么？"
        }
    ],
    "temperature": 0.7
}

# 发送请求
try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()  # 检查HTTP错误
    
    # 解析响应
    result = response.json()
    
    # 提取生成的文本
    if "content" in result:
        for item in result["content"]:
            if item["type"] == "text":
                print(item["text"])
    else:
        print("No content generated")
        print(result)
except Exception as e:
    print(f"Error: {e}")
    print(response.text if 'response' in locals() else "No response") 