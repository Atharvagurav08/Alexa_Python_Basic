import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone( ) as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'tom' in command:
                command = command.replace('tom','')
                talk(command)


    except:
        pass
    return command

def run_alexa():
    Command  = take_command()
    print(Command)
    if 'play' in Command:
        song = Command.replace('play','')
        talk('playing '+song)
        print('playing your song')
        pywhatkit.playonyt(song)
    elif 'time' in Command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The current time is '+time)
    elif 'who is ' in Command:
        person = Command.replace('who is ','')
        info = wikipedia.summary(person,20)
        print(info)
        talk(info)
    elif 'superman' in Command:
        sup = Command.replace('alexa','')
        sup = (Command)
        info = wikipedia.summary(sup,1)
        talk(info)
    elif 'joke' in Command:
        talk(pyjokes.get_joke())
    else:
        talk('say it again ')

while True:
    run_alexa()

