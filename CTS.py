import pyautogui
import pyperclip
import time

def ask_chatgpt(prompt):
    print(f"Asking ChatGPT: {prompt}")
    
    # Copy prompt to clipboard
    pyperclip.copy(prompt)
    
    # Pause to let you switch windows
    print("You have 5 seconds to switch to your browser window...")
    time.sleep(5)
    
    # Paste and send
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    print("Prompt sent!")

if __name__ == "__main__":
    user_input = input("Enter your command or question: ")
    ask_chatgpt(user_input)
