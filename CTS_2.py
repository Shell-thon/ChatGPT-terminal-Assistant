import speech_recognition as sr
import pyautogui
import pyperclip
import pyttsx3
import time

# Optional: Identify available microphones and print them
def list_microphones():
    print("\n🛠️ Available Microphones:")
    for i, mic_name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{i}: {mic_name}")
    print("Update 'device_index' accordingly.\n")

# Initialize recognizer and text-to-speech
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Choose your mic index here (change this after checking list)
DEVICE_INDEX = 1  # CHANGE THIS if needed

def speak(text):
    """Use TTS to read ChatGPT response"""
    tts_engine.say(text)
    tts_engine.runAndWait()

def send_to_chatgpt(prompt):
    """Send prompt to ChatGPT via clipboard + keyboard automation"""
    print("🧠 Sending prompt to ChatGPT...")
    pyperclip.copy(prompt)
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    print("✅ Prompt sent! Check your browser.")

def main():
    # List microphones once (optional)
    list_microphones()

    with sr.Microphone(device_index=DEVICE_INDEX) as source:
        print("🎙️ Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("🎧 Listening... (Speak now)")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("🔍 Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"✅ You said: {query}")

            # Send to ChatGPT
            send_to_chatgpt(query)
            speak("Your prompt has been sent to ChatGPT. Please check the browser.")

        except sr.UnknownValueError:
            print("❌ Sorry, I didn’t catch that. Try speaking clearly again.")
        except sr.RequestError as e:
            print(f"🔌 Network or API error: {e}")
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    main()
