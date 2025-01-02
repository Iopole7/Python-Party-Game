import os
from random import randint
from time import sleep
import pyautogui

from Games import helper_Functions
import sys,subprocess

def mem_game(engine, tts):
    running = True
    colours = ("g", "r", "b", "y")
    correct_guess = []
    correct_guess_string = ''
    guess = ""

    winner = -1
    team1Complete = False
    team2Complete = False
    team1Score = 0
    team2Score = 0
    team1Scoretemp = 0
    team2Scoretemp = 0

    starting_team = randint(1,2)

    s1 = "Welcome to memory mash! This game requires a full team to work together!"
    s2 = "Colours will be displayed on the screen and your team will have to memorize them!"
    s3 = "The team that can get the most right will win the round. The team that wins best 2/3 games gets the point."
    s4 = "Enter the colour sequence with the first letters ex. gbyygbr"
    s5 = f"The team starting first will be team {starting_team}"
    pyautogui.hotkey('ctrl', 'l')
    helper_Functions.pntSpeak(engine, tts, s1)
    helper_Functions.pntSpeak(engine, tts, s2)
    helper_Functions.pntSpeak(engine, tts, s3)
    helper_Functions.pntSpeak(engine, tts, s4)
    helper_Functions.pntSpeak(engine, tts, s5)
    input("Press enter to continue: ")
    while running:
        pyautogui.hotkey('ctrl', 'l')
        print("Next round")
        rnd_val = randint(0, 3)
        correct_guess.append(colours[rnd_val])
        correct_guess_string = ''.join(map(str, correct_guess))
        sleep(1)
        pyautogui.hotkey('ctrl','l')
        for val in correct_guess:
            if val == "g":
                helper_Functions.speak(engine, "green")
            elif val == "r":
                helper_Functions.speak(engine, "red")
            elif val == "b":
                helper_Functions.speak(engine, "blue")
            elif val == "y":
                helper_Functions.speak(engine, "yellow")
        print(correct_guess_string)
        guess = input("Colours:")
        if guess != correct_guess_string:
            helper_Functions.speak(engine, "Incorrect guess")
            if starting_team == 1:
                starting_team = 2
                team1Complete = True
                correct_guess.clear()
                if not team2Complete:
                    helper_Functions.speak(engine, f"It is team 2 turn")
            else:
                starting_team = 1
                team2Complete = True
                correct_guess.clear()
                if not team1Complete:
                    helper_Functions.speak(engine, f"It is team 1 turn")
        else:
            if starting_team == 1:
                team1Scoretemp += 1
            else:
                team2Scoretemp += 1

        if team1Complete and team2Complete:
            if team1Scoretemp > team2Scoretemp:
                team1Score += 1
                team1Complete = False
                team2Complete = False
                print("Team 1 won this round")
            elif team1Scoretemp < team2Scoretemp:
                team2Score += 1
                team1Complete = False
                team2Complete = False
                print("Team 2 won this round")
            else:
                print("Tie")
                team1Complete = False
                team2Complete = False

            helper_Functions.speak(engine, f"Team 1 got {team1Scoretemp} points, Team 2 got {team2Scoretemp} points")
            team1Scoretemp = 0
            team2Scoretemp = 0
            correct_guess.clear()
            if team1Score < 2 or team2Score < 2:
                helper_Functions.speak(engine, f"It is team {starting_team} turn now")
        else:
            pass
        if team1Score >= 2:
            print(f"Team 1 won the mini game! {team1Score}:{team2Score}")
            return 1
        if team2Score >= 2:
            print(f"Team 2 won the mini game! {team2Score}:{team1Score}")
            return 2








