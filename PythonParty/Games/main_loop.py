import pyttsx3
import helper_Functions
import keyboard

pointsToWin = 10
textInVal = 10
startCon = False
teamMode = ""
isTeam1 = True
playerIn = ""
playerIn2 = ""
playerIn1 = ""
team1 = []
team1String = ' '
team2 = []
team2String = ' '
players = []

impWord = ["start","quit","help"]

bst1 = "Hello and welcome to PPG, Python Party Game. You will all be split into two teams!"
bst2 = f"There are a series of mini games to complete and the first team to get {pointsToWin} points will be declared victorious."
bst3 = f"To access the help menu, type 'help' into the command line. To start the game, type 'start' into the command line."
bst4 = "To quit, press 'esc' on the keyboard, or type 'quit' into the command line."

gst1 = "Would you like to create teams manually, or automated? Type 'm' or 'a'"
gst2 = f"Alright, time to add the players! Add the players"
gst3 = "When done adding players for team1 type 'end'"
gst4 = "Now for team 2!"
gst5 = "List all the players! When done type 'end'!"

engine = pyttsx3.init()
engine.setProperty('rate', 190)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#helper_Functions.pntSpeak(engine, bst1)
#helper_Functions.pntSpeak(engine,bst2)
#helper_Functions.pntSpeak(engine,bst3)
#helper_Functions.pntSpeak(engine,bst4)

while True:
    if keyboard.is_pressed('esc'):
        break
    textIn = input('>').lower()
    if textIn in impWord:
        textInVal = impWord.index(textIn)
        if textInVal == 1:
            break
        elif textInVal == 0 and startCon == False:
            startCon = True
        elif textInVal == 0 and startCon == True:
            helper_Functions.pntSpeak(engine, "The game has already been started.")
        elif  textInVal == 2:
            helper_Functions.hlpMenu()
    else:
        textInVal = 10
        print("Invalid input")
    if startCon == True:
        helper_Functions.pntSpeak(engine, gst1)
        while teamMode != "m" and teamMode != "a":
            teamMode = input(">").lower()
            if teamMode != "m" and teamMode != "a":
                print("Invalid input")
        helper_Functions.pntSpeak(engine, gst2)
        if teamMode == "m":
            helper_Functions.pntSpeak(engine, gst3)
            while playerIn != "end":
                playerIn = input(">")
                team1.append(playerIn)
            helper_Functions.pntSpeak(engine, gst4)
            while playerIn2 != "end":
                playerIn2 = input(">")
                team2.append(playerIn2)
            team1.pop()
            team2.pop()
            team1String = ', '.join(map(str, team1))
            team2String = ', '.join(map(str, team2))
            print(team1String)
            print(team2String)
            helper_Functions.pntSpeak(engine, f"And that settles the teams! Team 1 is [{team1String}] and team 2 is [{team2String}]!")
            startCon = False
        if teamMode == "a":
            helper_Functions.pntSpeak(engine, gst5)
            while playerIn1 != "end":
                playerIn1 = input(">")
                players.append(playerIn1)
            players.pop()



helper_Functions.pntSpeak(engine, "Thank you for playing")
engine.stop()
