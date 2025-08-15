import speech_recognition as sr
import pyautogui
import pyperclip
import pyttsx3
import time
import platform
import wave  # For saving audio to WAV

# Initialize recognizer and text-to-speech
recognizer = sr.Recognizer()
try:
    tts_engine = pyttsx3.init()
    tts_engine.setProperty('rate', 150)
    tts_engine.setProperty('volume', 1.0)
except Exception as e:
    print(f"? Text-to-speech initialization failed: {e}")
    exit(1)

def list_microphones():
    """List available microphones"""
    try:
        mics = sr.Microphone.list_microphone_names()
        if not mics:
            print("? No microphones detected. Please check your audio devices.")
            return False, None
        print("\n??? Available Microphones:")
        for i, mic_name in enumerate(mics):
            print(f"{i}: {mic_name}")
        print("Select the microphone index to use (use Realtek for best results).\n")
        return True, mics
    except Exception as e:
        print(f"? Error listing microphones: {e}")
        return False, None

def speak(text):
    """Use TTS to read text"""
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        print(f"? Text-to-speech error: {e}")

def send_to_chatgpt(prompt):
    """Send prompt to ChatGPT via clipboard + keyboard automation"""
    print("?? Sending prompt to ChatGPT...")
    try:
        pyautogui.hotkey("alt", "tab")  # Switch to browser
        time.sleep(1)
        pyperclip.copy(prompt)
        time.sleep(1)
        if platform.system() == "Darwin":
            pyautogui.hotkey("command", "v")
        else:
            pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)
        pyautogui.press("enter")
        print("? Prompt sent! Check your browser.")
    except Exception as e:
        print(f"? Automation error: {e}")

def main():
    success, mics = list_microphones()
    if not success:
        exit(1)
    
    try:
        DEVICE_INDEX = int(input("Enter the microphone index (e.g., 6 for Realtek Microphone Array): "))
        if DEVICE_INDEX < 0 or DEVICE_INDEX >= len(mics):
            print(f"? Invalid index. Please select a number between 0 and {len(mics) - 1}.")
            exit(1)
    except ValueError:
        print("? Invalid input. Please enter a number.")
        exit(1)
    
    print("?? Press Enter to start listening, or Ctrl+C to exit. Speak loudly and clearly.")
    while True:
        input("Press Enter to listen...")
        try:
            with sr.Microphone(device_index=DEVICE_INDEX) as source:
                print("??? Adjusting for background noise (be quiet for 4 seconds)...")
                recognizer.adjust_for_ambient_noise(source, duration=4)
                recognizer.energy_threshold = 50  # Lower for quiet rooms/low volume mics
                print(f"Energy threshold set to: {recognizer.energy_threshold}")
                print("?? Listening... (Speak now for up to 15 seconds, speak loudly)")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)
                
                # Save audio for debugging
                with open("test_audio.wav", "wb") as f:
                    f.write(audio.get_wav_data())
                print("?? Saved captured audio to 'test_audio.wav' for debugging. Play it to check your voice.")
                
                print("?? Recognizing...")
                query = recognizer.recognize_google(audio)
                print(f"? You said: {query}")
                send_to_chatgpt(query)
                speak("Your prompt has been sent to ChatGPT. Please check the browser.")
        except sr.UnknownValueError:
            print("? Sorry, I didn't catch that. Try speaking louder/closer or check 'test_audio.wav'.")
        except sr.RequestError as e:
            print(f"?? Network or API error: {e}")
        except ValueError as e:
            print(f"? Invalid microphone index: {e}")
            exit(1)
        except KeyboardInterrupt:
            print("\n?? Stopping script. Goodbye!")
            break
        except Exception as e:
            print(f"?? Unexpected error: {e}")
        print("?? Press Enter to listen again or Ctrl+C to exit...")

if __name__ == "__main__":
    pyautogui.PAUSE = 0.5
    main()
