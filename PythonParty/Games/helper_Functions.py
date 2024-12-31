import pyttsx3

def pntSpeak(engine, state, speach):
    print(speach)
    if state:
        engine.say(speach)
        engine.runAndWait()

def hlpMenu():
    print("To start the game, type 'start', To quit, type 'quit'")


