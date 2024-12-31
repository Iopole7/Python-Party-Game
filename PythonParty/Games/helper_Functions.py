import pyttsx3
def pntSpeak(engine, speach):
    print(speach)
    engine.say(speach)
    engine.runAndWait()

def hlpMenu():
    print("To start the game, type 'start', To quit, type 'quit'")


