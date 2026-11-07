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

<h2>五、本地 vs 雲端 LLM 比較表</h2>
<table border="1" style="border-collapse: collapse; width: 100%; text-align: left;">
    <tr style="background-color: #edf2f7;">
        <th style="padding: 8px;">比較項目</th>
        <th style="padding: 8px;">本地模型 (如 Ollama / Llama 3)</th>
        <th style="padding: 8px;">雲端 API (如 Gemini 2.5 Flash)</th>
    </tr>
    <tr>
        <td style="padding: 8px;"><b>回應速度與算力</b></td>
        <td style="padding: 8px;">依賴本機 GPU/RAM，速度受硬體限制</td>
        <td style="padding: 8px;">雲端算力強大，回應迅速且支援串流 (Streaming)</td>
    </tr>
    <tr>
        <td style="padding: 8px;"><b>資料安全性</b></td>
        <td style="padding: 8px;">100% 本地運算，資料不外洩</td>
        <td style="padding: 8px;">需透過 API 送出傳輸，需防護 API Key 機敏資料</td>
    </tr>
    <tr>
        <td style="padding: 8px;"><b>部署與維護成本</b></td>
        <td style="padding: 8px;">無需 API Key，但需配置本地環境</td>
        <td style="padding: 8px;">免安裝大模型，隨插即用，適合自動化 CI/CD 部署</td>
    </tr>
</table>