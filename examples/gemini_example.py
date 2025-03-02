# Gemini API调用示例
# 使用代理访问Google Gemini API

import requests
import json

# 配置
PROXY_URL = "https://your-worker.workers.dev"  # 替换为您的Worker URL
API_KEY = "your-gemini-api-key"  # 替换为您的Gemini API密钥

# 构建请求
url = f"{PROXY_URL}/gemini/v1beta/models/gemini-pro:generateContent"
headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY
}

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "介绍一下量子计算的基本原理"
                }
            ]
        }
    ],
    "generationConfig": {
        "temperature": 0.7,
        "maxOutputTokens": 500
    }
}

# 发送请求
try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()  # 检查HTTP错误
    
    # 解析响应
    result = response.json()
    
    # 提取生成的文本
    if "candidates" in result and len(result["candidates"]) > 0:
        generated_text = result["candidates"][0]["content"]["parts"][0]["text"]
        print(generated_text)
    else:
        print("No content generated")
        print(result)
except Exception as e:
    print(f"Error: {e}")
    print(response.text if 'response' in locals() else "No response") 