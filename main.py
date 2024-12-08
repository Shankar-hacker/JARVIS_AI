import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#todo:add new feature

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 2000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shankarpaikira225@gmail.com', 'Shankar 0034#@')
    server.sendmail('shankarpaikira225@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speak("opening stack overflow")
            webbrowser.open("stackoverflow.com")

        elif 'hu r u' in query:
            speak("I am Jarvis Sir. Please tell me how may I help you")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\shankar paikira\\Music\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, random_song))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'quit' in query:
            exit()

        elif 'open code' in query:
            codePath = 'C:\\Users\\shankar paikira\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)

        elif 'open word' in query:
            codePath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe'
            os.startfile(codePath)

        elif 'open ppt' in query:
            codePath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
            os.startfile(codePath)

        elif 'open whatsapp' in query:
            codePath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
            os.startfile(codePath)

        elif 'play online music' in query:
            speak("playing music")
            webbrowser.open("https://music.youtube.com/watch?v=2nR1zrNzgcY")

        elif 'play Enna Sona' in query:
            speak("playing")
            webbrowser.open("https://music.youtube.com/watch?v=r89zj42xDOo")


        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "surjaykumar0@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend shankar bhai. I am not able to send this email")
