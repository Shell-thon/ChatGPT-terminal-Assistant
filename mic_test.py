import speech_recognition as sr

def test_microphones():
    recognizer = sr.Recognizer()

    print("🛠️ Starting microphone test...")
    for index in [1, 5, 9, 10]:  # Try common real mic indexes on your system
        print(f"\n🎤 Testing Microphone Index: {index}")
        try:
            with sr.Microphone(device_index=index) as source:
                print("🔧 Adjusting for ambient noise...")
                recognizer.adjust_for_ambient_noise(source, duration=1)

                recognizer.pause_threshold = 0.5
                print("🎧 Listening... (Speak now)")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)


                print("🔍 Recognizing speech...")
                text = recognizer.recognize_google(audio)
                print(f"✅ Index {index} worked! You said: \"{text}\"")

        except sr.UnknownValueError:
            print(f"⚠️ Index {index} heard something but couldn't understand it.")
        except sr.RequestError as e:
            print(f"❌ Network/API error: {e}")
        except Exception as e:
            print(f"❌ Error with index {index}: {e}")

if __name__ == "__main__":
    test_microphones()
