import pyttsx3  # speak
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

jarvis = pyttsx3.init()

# get/set voice
voice = jarvis.getProperty('voices')
jarvis.setProperty('voice', voice[1].id)

def speak(audio):
    print('JARVIS: ' + audio)
    jarvis.say(audio)
    jarvis.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M %p")  # I - hour | M - min | p - Am/PM
    speak(Time+", Sir")

def welcome():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir")
    elif 18 <= hour < 24:
        speak("Good Night Sir")
    speak("How can I help you")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        c.pause_threshold = 2  # stop 2 seconds when listening to command
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language="en")
        print("User(KHOA): " + query)
    except sr.UnknownValueError:
        print("Please repeat or type the command")
        query = str(input("Your order is: "))
    return query

if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("What should I search for, boss?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on Google")
        if "youtube" in query:
            speak("What should I search for, boss?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on Youtube")
        elif "time" in query:
            time()
        elif "goodbye" in query:
            speak("Goodbye, Sir! Jarvis signing off. Have a great day!")
            quit()         
