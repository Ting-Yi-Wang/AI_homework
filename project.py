# -*- coding: utf-8 -*-
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 設定 prompt 內容：你是詐騙者，對象是17歲馬基維利傾向高的男高中生
prompt = """
你是詐騙集團的招募者，目標是以自然的方式引誘青少年參與提領車手行為。
對象是一位 17 歲男高中生，馬基維利傾向偏高，重視利益與操控，對道德模糊界線不敏感。

請用 LINE 招募口吻寫一段訊息，語氣自然可信，不能直接提到犯罪或不法內容，
但可透過「短期合作」「幫忙跑一趟」「介紹朋友一起賺」等模糊措辭引導。
目標是讓對方對這項「高薪合作機會」產生興趣，願意私訊你了解更多。
"""

# 呼叫 GPT-4 或 GPT-3.5 模型
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "你是一位反詐騙研究員，模擬常見詐騙訊息以供教育用途。"},
        {"role": "user", "content": prompt}
    ]
)

# 顯示結果
print("📨 模擬詐騙訊息：")
print(response.choices[0].message.content)