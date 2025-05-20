# -*- coding: utf-8 -*-
from openai import OpenAI
from dotenv import load_dotenv
import os
import gradio as gr

# 載入環境變數
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 系統角色與提示
system_msg = "你是一位反詐騙研究員，模擬詐騙訊息對話流程，僅用於教育與防詐教學用途。"
first_prompt = """
請模擬一段詐騙集團的招募訊息，單方面傳送給一位 17 歲男高中生，內容需使用模糊措辭誘導對方產生興趣。
語氣應自然可信，有如透過 LINE 傳送，並讓對方覺得這是一項輕鬆又能賺快錢的短期合作機會。
可使用如「幫忙跑一趟」「介紹朋友一起賺」「穩定又自由」等字眼，**但不能明示犯罪、不法或暴力行為**。
僅產出一段完整的詐騙者訊息，不要進行對話模擬。
"""

# 儲存對話
chat_history = []

# 初始產生詐騙訊息
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
    chat_history.append({"role": "assistant", "content": scam_msg})
    return scam_msg

# 處理使用者輸入並回覆
def continue_dialogue(user_input):
    messages = [{"role": "system", "content": system_msg}]
    messages.append({"role": "user", "content": first_prompt})
    for entry in chat_history:
        messages.append(entry)
    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response.choices[0].message.content
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": reply})
    return reply

# 最後產出防詐建議
def generate_advice():
    dialogue = "這是一段模擬詐騙對話，目標對象為一位 17 歲男高中生：\n\n"
    for i, msg in enumerate(chat_history):
        role = "詐騙者" if msg["role"] == "assistant" else "使用者"
        dialogue += f"{role}：\n{msg['content']}\n\n"

    advice_prompt = f"""
{dialogue}
請你根據這段模擬對話，提供青少年防止詐騙的具體建議（例如：警示語氣、識破關鍵點、應對方式），不需重述對話，只需給出清楚的反詐建議。
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一位反詐騙教育顧問，請根據模擬對話給出具體的防詐建議。"},
            {"role": "user", "content": advice_prompt}
        ]
    )
    return response.choices[0].message.content

# Gradio 介面
with gr.Blocks() as demo:
    gr.Markdown("# 🕵️‍♂️ 錢途陷阱模擬對話")
    
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(label="請輸入你的回覆")
    
    with gr.Row():
        send_btn = gr.Button("送出")
        advice_btn = gr.Button("🛡️ 產出防詐建議")
        restart_btn = gr.Button("🔄 重新模擬")

    def on_send(user_msg):
        reply = continue_dialogue(user_msg)
        msgs = []
        for entry in chat_history:
            role = "詐騙者" if entry["role"] == "assistant" else "你"
            msgs.append((role, entry["content"]))
        return msgs, ""

    def on_restart():
        msg = start_simulation()
        return [("詐騙者", msg)], ""

    send_btn.click(on_send, inputs=user_input, outputs=[chatbot, user_input])
    advice_btn.click(generate_advice, outputs=chatbot)
    restart_btn.click(on_restart, outputs=[chatbot, user_input])

# 啟動
if __name__ == "__main__":
    demo.launch()