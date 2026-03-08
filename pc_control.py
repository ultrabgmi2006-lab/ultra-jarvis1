import os
import webbrowser
import pyautogui

def handle_pc_command(command):

    if "open chrome" in command:
        os.system("start chrome")
        return True

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return True

    elif "close window" in command:
        pyautogui.hotkey("alt","f4")
        return True

    elif "shutdown computer" in command:
        os.system("shutdown /s /t 5")
        return True

    return False
