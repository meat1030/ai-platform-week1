# 📊 AI 股票與 ETF 投資分析助手 (ai-platform-week1)

## 📌 專案簡介
本專案為 AI 平台開發作業，結合 Python 與 Google Gemini API (gemini-2.5-flash)，實作具備串流回應功能的投資分析工具，並透過 GitHub Actions 自動部署作品頁。

## 🚀 執行步驟
1. 複製專案：`git clone https://github.com/meat1030/ai-platform-week1.git`
2. 配置金鑰：建立 `.env` 並設定 `LLM_API_KEY=your_key`
3. 安裝依賴：`pip install google-genai python-dotenv`
4. 執行測試：`python app.py`

## 🛡️ 安全說明
機敏資訊 `.env` 檔案已列入 `.gitignore` 防護，絕不出現在版本控制與 Commit 歷史中。