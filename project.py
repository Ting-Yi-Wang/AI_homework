# -*- coding: utf-8 -*-
from openai import OpenAI
from dotenv import load_dotenv
import os

# 載入環境變數
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 系統角色
system_msg = "你是一位反詐騙研究員，模擬詐騙訊息對話流程，僅用於教育與防詐教學用途。"

# 初始提示
first_prompt = """
請模擬一段詐騙集團的招募訊息，單方面傳送給一位 17 歲男高中生，內容需使用模糊措辭誘導對方產生興趣。
語氣應自然可信，有如透過 LINE 傳送，並讓對方覺得這是一項輕鬆又能賺快錢的短期合作機會。
可使用如「幫忙跑一趟」「介紹朋友一起賺」「穩定又自由」等字眼，**但不能明示犯罪、不法或暴力行為**。
僅產出一段完整的詐騙者訊息，不要進行對話模擬。
"""

# ✅ 第 1 輪：詐騙者開場
response1 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_msg},
        {"role": "user", "content": first_prompt}
    ]
)
first_message = response1.choices[0].message.content
print("📨 第1輪詐騙者訊息：\n", first_message)

# ✅ 使用者第 2 輪回覆
user_input_1 = input("\n🧑 使用者回覆（第2輪）：\n")

# ✅ 第 2 輪：詐騙者回應
response2 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_msg},
        {"role": "user", "content": first_prompt},
        {"role": "assistant", "content": first_message},
        {"role": "user", "content": user_input_1}
    ]
)
second_message = response2.choices[0].message.content
print("\n📨 第2輪詐騙者訊息：\n", second_message)

# ✅ 使用者第 3 輪回覆
user_input_2 = input("\n🧑 使用者回覆（第3輪）：\n")

# ✅ 第 3 輪：詐騙者回應
response3 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_msg},
        {"role": "user", "content": first_prompt},
        {"role": "assistant", "content": first_message},
        {"role": "user", "content": user_input_1},
        {"role": "assistant", "content": second_message},
        {"role": "user", "content": user_input_2}
    ]
)
third_message = response3.choices[0].message.content
print("\n📨 第3輪詐騙者訊息：\n", third_message)

# ✅ 使用者第 4 輪回覆
user_input_3 = input("\n🧑 使用者回覆（第4輪）：\n")

# ✅ 第 4 輪：詐騙者回應
response4 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_msg},
        {"role": "user", "content": first_prompt},
        {"role": "assistant", "content": first_message},
        {"role": "user", "content": user_input_1},
        {"role": "assistant", "content": second_message},
        {"role": "user", "content": user_input_2},
        {"role": "assistant", "content": third_message},
        {"role": "user", "content": user_input_3}
    ]
)
fourth_message = response4.choices[0].message.content
print("\n📨 第4輪詐騙者訊息：\n", fourth_message)

# ✅ 最後：請 AI 針對上述整段對話，給出防詐騙建議
print("\n🛡️ 正在分析防詐建議...\n")

# 組合整段對話紀錄供 AI 分析
dialogue_summary = f"""
這是一段模擬詐騙對話，目標對象為一位 17 歲男高中生：

第1輪（詐騙者）：
{first_message}

第2輪（使用者）：
{user_input_1}

第2輪（詐騙者）：
{second_message}

第3輪（使用者）：
{user_input_2}

第3輪（詐騙者）：
{third_message}

第4輪（使用者）：
{user_input_3}

第4輪（詐騙者）：
{fourth_message}

請你根據這段模擬對話，提供青少年防止詐騙的具體建議（例如：警示語氣、識破關鍵點、應對方式），不需重述對話，只需給出清楚的反詐建議。
"""

response_advice = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "你是一位反詐騙教育顧問，請根據模擬對話給出具體的防詐建議。"},
        {"role": "user", "content": dialogue_summary}
    ]
)

advice = response_advice.choices[0].message.content
print("\n🛡️ 防詐騙建議：\n")
print(advice)