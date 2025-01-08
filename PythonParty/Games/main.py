from itertools import count
from random import shuffle, randint
from turtledemo.penrose import start

import pyttsx3
import helper_Functions
import random

from Games.Trivia import trivia_game
from Games.memory_mash import mem_game
from Games.objRet import obj_game
from Games.wordScramble import word_game


def sout(eng, tts, string):
    helper_Functions.pntSpeak(eng, tts, string)

pointsToWin = 3
textInVal = 10
startCon = False
teamMode = ""
isTeam1 = True
playerIn = ""
playerIn1 = ""
playerIn2 = ""
team1 = []
team1String = ' '
team2 = []
team2String = ' '
players = []
playerCount = 0
mainState = True
ttsON = True
reroll = "r"
team1P = 0
team2P = 0
ranGame = [0,1,2,3]
currGame = -1
canCon = False
counter = 0
mgame_winner = 0
rematch = False
endCon = False

impWord = ["start","quit","help"]
games = ["trivia", "object retrieval", "word scramble", "memory mash"]

bst1 = "Hello and welcome to PPG, Python Party Game. You will all be split into two teams!"
bst1_1 = "Please type 'on' and press enter to keep text to speech. Otherwise, press 'enter' to continue."
bst2 = f"There are a series of mini games to complete and the first team to get {pointsToWin} points will be declared victorious."
bst3 = f"To access the help menu, type 'help' into the command line. To start the game, type 'start' into the command line."
bst4 = "To quit, type 'quit' into the command line."

gst1 = "Would you like to create teams manually, or automatically? Type 'm' or 'a'"
gst2 = f"Alright, time to add the players! Type the name of one player into the line and press enter."
gst3 = "When done adding players for team1 type 'end'"
gst4 = "Now for team 2!"
gst5 = "List all the players! When done type 'end'!"

sst1 = f"\nNow time to play!\n"

engine = pyttsx3.init()
engine.setProperty('rate', 190)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

sout(engine,ttsON,  bst1)
sout(engine,ttsON, bst1_1)
ttsState = input(">").lower()
if ttsState != "on":
    ttsON = False
sout(engine, ttsON, bst2)
sout(engine, ttsON, bst3)
sout(engine, ttsON, bst4)

while mainState:
    if teamMode == "quit":
        break
    if not rematch:
        textIn = input('>').lower()
    if textIn in impWord:
        textInVal = impWord.index(textIn)
        if textInVal == 1:
            break
        elif textInVal == 0 and startCon == False:
            startCon = True
        elif textInVal == 0 and startCon == True:
            sout(engine,  ttsON, "The game has already been started.")
        elif  textInVal == 2:
            helper_Functions.hlpMenu()
    else:
        textInVal = 10
        print("Invalid input")

    if startCon:
        sout(engine, ttsON, gst1)
        while teamMode != "m" and teamMode != "a" and mainState:
            teamMode = input(">").lower()
            if teamMode == "quit":
                mainState = False
            elif teamMode == "help":
                helper_Functions.hlpMenu()
            elif teamMode != "m" and teamMode != "a":
                print("Invalid input")
        if teamMode == "m":
            sout(engine, ttsON, gst2)
            sout(engine, ttsON, gst3)
            while playerIn != "end":
                playerIn = input(">")
                team1.append(playerIn)
                playerCount += 1
            sout(engine, ttsON, gst4)
            while playerIn2 != "end":
                playerIn2 = input(">")
                team2.append(playerIn2)
                playerCount += 1
            team1.pop()
            team2.pop()
            team1String = ', '.join(map(str, team1))
            team2String = ', '.join(map(str, team2))
            sout(engine, ttsON, f"And that settles the teams! Team 1 is [{team1String}] and team 2 is [{team2String}]!")

        if teamMode == "a":
            sout(engine,  ttsON,gst2)
            sout(engine, ttsON, gst5)
            while playerIn1 != "end":
                playerIn1 = input(">")
                players.append(playerIn1)
                playerCount += 1
            players.pop()
            playerCount-= 1
            random.shuffle(players)
            team1 = players[:playerCount//2]
            team2 = players[playerCount//2:]
            team1String = ', '.join(map(str, team1))
            team2String = ', '.join(map(str, team2))
            sout(engine, ttsON,
                                      f"And that settles the teams! Team 1 is [{team1String}] and team 2 is [{team2String}]!")
            reroll = input("If you would like to shuffle the teams type 'r'. Press anything else to continue. >")
            while reroll == "r":
                random.shuffle(players)
                team1 = players[:playerCount // 2]
                team2 = players[playerCount // 2:]
                team1String = ', '.join(map(str, team1))
                team2String = ', '.join(map(str, team2))
                sout(engine, ttsON,
                                          f"Team 1 is [{team1String}] and team 2 is [{team2String}]!")
                reroll = input("Press 'r' to reroll. Press anything else to continue. >")
        startCon = False
        sout(engine, ttsON, sst1)
        shuffle(ranGame)
        canCon = True
    while pointsToWin > team1P and pointsToWin > team2P and canCon:
        sout(engine, ttsON, f"Team 1 has won {team1P} games and team 2 has won {team2P} games. Press enter to start the next game!")
        input(">")
        if counter == 4:
            sout(engine, ttsON, f"The score is tied! So we have a tie breaker game!")
            currGame = randint(0, 3)
            input("Press enter when ready: ")
        else:
            currGame = ranGame[counter]
        counter += 1
        if currGame == 0:
            mgame_winner = trivia_game(engine, ttsON)
        elif currGame == 1:
            mgame_winner = obj_game(engine, ttsON, team1, team2)
        elif currGame == 2:
            mgame_winner = word_game(engine, ttsON)
        elif currGame == 3:
            mgame_winner = mem_game(engine, ttsON)

        if mgame_winner == 1:
            team1P += 1
            mgame_winner = -1
        elif mgame_winner == 2:
            team2P += 1
            mgame_winner = -1
    if endCon:
        if team1P > team2P:
            sout(engine, ttsON, "Team 1 won! YAYAY")
        else:
            sout(engine, ttsON, "Team 2 won! YAYAY")
        if input("Rematch? Enter 'y' to rematch: ") == 'y':
            team1P = 0
            team2P = 0
            canCon = True
            rematch = True
            counter = 0
            shuffle(ranGame)
        else:
            break

sout(engine, ttsON,"\nThank you for playing")
engine.stop()
