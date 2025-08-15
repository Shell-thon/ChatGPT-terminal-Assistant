# 🧠 ChatGPT Terminal Assistant No API Required

This is a lightweight Python script that lets you interact with ChatGPT directly from your terminal **without using an API key**.

Instead of relying on OpenAI's API (with keys, limits, and billing), this assistant hijacks the **ChatGPT web interface** using simple clipboard and GUI automation.

---

## 🚀 Features

- Send terminal queries directly to ChatGPT (via the browser)
    
- No API key needed
    
- Super lightweight (just Python and a few libraries)
    
- Works with free ChatGPT accounts
    

---

## 📦 Requirements

- Python 3.7+
    
- ChatGPT account (free is fine)
    
- Browser tab with [chat.openai.com](https://chat.openai.com/) open and logged in
    

Install dependencies:

```bash
pip install pyautogui pyperclip SpeechRecognition pyttsx3 pyaudio
```

---

### ✅ `CTS.py`

> Basic terminal assistant  
> Send questions to ChatGPT using clipboard + keyboard automation.

📰 [Read the article](https://medium.com/python-in-plain-english/build-a-chatgpt-terminal-assistant-with-python-no-api-required-e52b91953d38)

---

### 🎙️ `CTS_2.py`

> Voice-powered assistant  
> Speak your questions, send them to ChatGPT, and get the response read out loud — all without using the API.  
> Perfect for when your hands are busy or you just want to feel like Jarvis is listening.

📰 [Read Part 2](https://chatgpt.com/c/comingsoon)

---

## 🧠 Features

- No API key required
    
- Works with the free ChatGPT account
    
- Terminal + voice input
    
- Text-to-speech responses
    
- Great for DevOps, automation, and smart scripting
    

---

## 🛠️ How to Use

1. Open `chat.openai.com` and log in
    
2. Run either script:
    

```bash
python CTS.py   # Text mode  
python CTS_2.py # Voice mode  
```

3. Follow on-screen instructions (type or speak your prompt)
    
4. Switch to your browser within 5 seconds
    
5. View ChatGPT’s response
    

---

## 📜 Changelog

**v2.0 – CTS_2.py**

- Added voice input using `SpeechRecognition`
    
- Added text-to-speech replies via `pyttsx3`
    
- Cleaner code and faster switching
    
- Retired the old `vn.py` test script
    

---

## 🧑‍💻 Author

Built by [Michael] — sharing daily Python, DevOps, and AI automation tools.  
📰 Medium: [@shell-terminal](https://medium.com/@shell-terminal)  
🐦 X: [@michaeldev0ps](https://twitter.com/michaeldev0ps)  
🔗 [LinkedIn](https://www.linkedin.com/in/michaeldev0ps/)

---
