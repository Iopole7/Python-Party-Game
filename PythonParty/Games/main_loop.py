import time
import pyttsx3
import helper_Functions
import keyboard


pointsToWin = 10

bst1 = "Hello and welcome to PPG, Python Party Game. You will all be split into two teams!"
bst2 = f"There are a series of mini games to complete and the first team to get {pointsToWin} points will be declared victorious."
bst3 = f"To access the help menu, type 'help' into the command line. To start the game, type 'start' into the command line."
bst4 = "To quit, type 'quit' into the command line."

engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

helper_Functions.pntSpeak(engine, bst1)
helper_Functions.pntSpeak(engine,bst2)
helper_Functions.pntSpeak(engine,bst3)
helper_Functions.pntSpeak(engine,bst4)

while True:
    textIn = input('>')
    




engine.stop()
