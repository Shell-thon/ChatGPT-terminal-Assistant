#!/usr/bin/env

import pyautogui
import pyperclip
import speech_recognition as sr
import pyttsx3
import time

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening... (Speak now)")
        audio = recognizer.listen(source)
    try:
        prompt = recognizer.recognize_google(audio)
        print(f"You said: {prompt}")
        return prompt
    except sr.UnknownValueError:
        print("Sorry, I didn’t catch that.")
        return None

def speak_response(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def send_to_chatgpt(prompt):
    pyperclip.copy(prompt)
    print("⏳ Switching to browser... you have 5 seconds.")
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    print("✅ Prompt sent to ChatGPT.")

if __name__ == "__main__":
    prompt = listen_to_user()
    if prompt:
        send_to_chatgpt(prompt)
        print("💬 Now switch to ChatGPT to see the reply.")
        response = input("Paste the reply here if you want it read aloud: ")
        if response:
            speak_response(response)

