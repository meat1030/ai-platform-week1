import os
from dotenv import load_dotenv
from google import genai

# 載入 .env 機敏設定
load_dotenv()
api_key = os.getenv("LLM_API_KEY")

if not api_key:
    raise ValueError("找不到 LLM_API_KEY，請確認 .env 檔案內容！")

# 初始化 Google GenAI Client
client = genai.Client(api_key=api_key)

print("=== 📊 AI 股票與 ETF 投資分析助手 ===")
stock_name = input("請輸入欲分析的股票名稱或標的 (例如: 台中銀 / 中信金 / 0050): ")

prompt = f"請針對 '{stock_name}' 進行簡短的投資特色分析，回覆包含：1. 核心優勢 2. 潛在風險 3. 投資建議。"

print("\n🤖 AI 正在進行分析與串流輸出中...\n")
response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=prompt,
)

for chunk in response:
    print(chunk.text, end="", flush=True)

print("\n\n✅ 分析完成！")