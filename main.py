import pyttsx3
from voice_engine import listen
from pc_control import handle_pc_command
from ai_brain import ask_ai
from config import WAKE_WORD

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

speak("Ultra Jarvis online")

while True:

    text = listen()

    if WAKE_WORD not in text:
        continue

    command = text.replace(WAKE_WORD,"").strip()

    if handle_pc_command(command):
        speak("Command executed")
        continue

    answer = ask_ai(command)

    speak(answer)
