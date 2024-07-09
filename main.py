import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d093053d72bc40248998159804e0e67d"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com") 
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com") 
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r= requests.get(f"http://newsapi.org/v2/top-headlines?country=in&apikey={newsapi}")
        if r.status_code == 200:
            data = r.json() 
            articles = data.get('articles',[])

            for article in articles:    
                speak(article['title'])

if __name__=="__main__":
    speak("Initializg Jarvis....")

    while True:
        # Listen for the wake word Jarvis
        # obtain audio from the microphone
        r=sr.Recognizer()
          
        # recognize speech using google
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening.. !")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)

            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("ya")
                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis active.. !")
                    audio=r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)


        except Exception as e:
            print("Error")