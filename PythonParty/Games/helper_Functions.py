import pyttsx3
def pntSpeak(engine, speach):
    print(speach)
    engine.say(speach)
    engine.runAndWait()