

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1

        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio,language='en-in')
            print(" You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("Speech service error.")
            speak("Sorry, my speech service is down.")
            return ""

def run_assistant():
    speak("Hello! I'm your virtual assistant. How can I help you?")
    while True:
        command = input()

        if 'weather' in command:
        
            speak(f"The weather is too good today")
            
        elif 'play chess' in command:
            speak(" ohh lets play the chess")
        
        elif 'Today news in ap' in command:
            speak(" their are differnt news across the ap")

        elif 'open spotify' in command:
            speak("Opening spotify")
            webbrowser.open("https://open.spotify.com/")

        elif 'youtube' in command:
            speak("for audi and videos")
            webbrowser.opan("https://www.youtube.com")

        elif 'stop' in command or 'exit' in command or 'bye' in command:
            speak("Okay bye bye! Have a good day")
            break

        else:
            speak("Sorry, I can't do that yet.")

# Run the assistant
run_assistant()