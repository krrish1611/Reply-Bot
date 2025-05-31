# 🤖 WhatsApp Chatbot Automation using OpenAI GPT

A Python-based automation script that uses **OpenAI's GPT-3.5 Turbo** to read and respond to WhatsApp messages in real-time. Built for a bilingual (Hindi + English) personality named **Krrish**, this bot adds a human-like conversational flow to your WhatsApp chats.

---

## 🧩 Project Overview

### This project:
- 📋 Reads the most recent message from a WhatsApp web chat.
- 🧠 Sends it to OpenAI GPT to generate a personalized reply.
- 📨 Automatically types and sends the reply via the WhatsApp chat window.

It combines the power of **AI-generated text** and **GUI automation** to create a seamless chatbot experience.

---

## 📁 Folder Structure

| File         | Description                                                  |
|--------------|--------------------------------------------------------------|
| `main.py`    | Main automation loop: reads, generates, and sends replies.   |
| `client.py`  | Standalone example for testing GPT responses.                |
| `program.py` | Helper to determine screen coordinates using pyautogui.      |
| `.gitattributes` | Git config for consistent line endings across platforms. |

---

## 🔧 Requirements

- Python 3.x
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [`pyautogui`](https://pypi.org/project/PyAutoGUI/)
- [`pyperclip`](https://pypi.org/project/pyperclip/)

### 📦 Install Dependencies
```bash
pip install openai pyautogui pyperclip
```
## 🚀 Setup Guide
### 🔑 Add your OpenAI API Key
In both main.py and client.py, replace:
```
api_key = ""  
```
Replace with your OpenAI API key

---
## 🖱️ Adjust Screen Coordinates
Use program.py to find the exact screen coordinates for:

Opening WhatsApp window

Selecting and copying the chat

Clicking the input field

Update those values in main.py accordingly.

---

## ▶️ Run the Bot
```
python main.py
```
Keep WhatsApp Web open in a browser tab and make sure the coordinates match.

---

## 💬 Customization
Modify the personality or tone by editing the system message inside the messages array:
```
{"role": "system", "content": "You are a person named Krrish who speaks Hindi and English..."}
Adjust the message parsing logic if your WhatsApp format differs.
```
Edit this as per your requirement

---


## ⚠️ Disclaimer
🛑 This script is for personal and educational purposes only.
🧾 Automating messaging may violate WhatsApp’s Terms of Service. Use responsibly.

---

## 📄 License
Licensed under the MIT License.
Feel free to modify and build upon this project!

---

## ✨ Author
**Krrish Sah**  
💻 Developer | 🤖 AI Enthusiast | 🇮🇳 From India

---
