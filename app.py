# -*- coding: utf-8 -*-
from openai import OpenAI
from dotenv import load_dotenv
import os
import gradio as gr

# 載入環境變數
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 系統角色與提示
system_msg = "你是一位打工陷阱的研究員，模擬打工陷阱對話流程，僅用於教育與防詐教學用途。"
first_prompt = """
請模擬一段打工陷阱的招募訊息，單方面傳送給一位 17 歲男高中生，內容需使用模糊措辭誘導對方產生興趣。
語氣應自然可信，有如透過 LINE 傳送，並讓對方覺得這是一項輕鬆又能賺快錢的短期合作機會。
可使用如「幫忙跑一趟」「介紹朋友一起賺」「穩定又自由」等字眼，但不能明示犯罪、不法或暴力行為。
僅產出一段完整的招募者訊息，不要進行對話模擬。
"""

# 儲存對話
chat_history = []  # 傳給 OpenAI 的格式
ui_history = []    # Gradio messages 格式 (list of {"role", "content"})

# 初始招募訊息（單向）
def start_simulation():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": first_prompt}
        ]
    )
    scam_msg = response.choices[0].message.content
    chat_history.clear()
    ui_history.clear()

    chat_history.append({"role": "assistant", "content": scam_msg})
    ui_history.append({"role": "assistant", "content": scam_msg})  # ✅ type='messages'

    return ui_history, ""

# 使用者輸入並得到回應
def on_send(user_msg):
    messages = [{"role": "system", "content": system_msg}]
    messages.append({"role": "user", "content": first_prompt})
    messages.extend(chat_history)
    messages.append({"role": "user", "content": user_msg})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response.choices[0].message.content

    chat_history.append({"role": "user", "content": user_msg})
    chat_history.append({"role": "assistant", "content": reply})
    ui_history.append({"role": "user", "content": user_msg})
    ui_history.append({"role": "assistant", "content": reply})

    return ui_history, ""

# 產生反詐建議
def generate_advice():
    dialogue = ""
    for msg in chat_history:
        role = "招募者" if msg["role"] == "assistant" else "使用者"
        dialogue += f"{role}：\n{msg['content']}\n\n"

    advice_prompt = f"""
{dialogue}
請你根據這段模擬對話，提供青少年防止打工陷阱的具體建議（例如：警示語氣、識破關鍵點、應對方式），不需重述對話，只需給出清楚的反詐建議。
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一位反打工陷阱顧問，請根據模擬對話給出具體的識別陷阱建議。"},
            {"role": "user", "content": advice_prompt}
        ]
    )
    advice = response.choices[0].message.content
    ui_history.append({"role": "assistant", "content": f"🛡️ 系統建議：\n{advice}"})
    return ui_history

# Gradio 介面
with gr.Blocks() as demo:
    gr.Markdown("## 🕵️‍♂️ 錢途陷阱模擬對話（教育用途）")

    chatbot = gr.Chatbot(label="對話視窗", type="messages")
    user_input = gr.Textbox(label="🧑 使用者輸入", placeholder="輸入你的回覆...")

    with gr.Row():
        send_btn = gr.Button("送出")
        advice_btn = gr.Button("🛡️ 產出建議")
        restart_btn = gr.Button("🔄 重新模擬")

    send_btn.click(fn=on_send, inputs=user_input, outputs=[chatbot, user_input])
    advice_btn.click(fn=generate_advice, outputs=chatbot)
    restart_btn.click(fn=start_simulation, outputs=[chatbot, user_input])

# 執行
if __name__ == "__main__":
    demo.launch(share=True)
