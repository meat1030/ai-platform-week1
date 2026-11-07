import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("LLM_API_KEY")
model_name = os.getenv("LLM_MODEL")

print("=== .env 讀取測試 ===")
print(f"API Key 讀取狀態: {'成功' if api_key else '失敗'}")
print(f"使用的模型: {model_name}")