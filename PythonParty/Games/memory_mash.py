from random import randint
from time import sleep

from Games import helper_Functions
import pygame
def mem_game(engine, tts):
    running = True
    colours = ("g", "r", "b", "y")
    correct_guess = []
    correct_guess_string = ''.join(map(str, correct_guess))
    guess = ""

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

    helper_Functions.pntSpeak(engine, tts, s1)
    helper_Functions.pntSpeak(engine, tts, s2)
    helper_Functions.pntSpeak(engine, tts, s3)
    helper_Functions.pntSpeak(engine, tts, s4)
    helper_Functions.pntSpeak(engine, tts, s5)

    while running:
        rnd_val = randint(0, 3)
        correct_guess.append(colours[rnd_val])
        input("Press enter when ready: ")
        sleep(1)
        for val in correct_guess:
            sleep(0.25)
            if val == "g":
                helper_Functions.speak(engine, "green")
            elif val == "r":
                helper_Functions.speak(engine, "red")
            elif val == "b":
                helper_Functions.speak(engine, "blue")
            elif val == "y":
                helper_Functions.speak(engine, "yellow")
        guess = input("Colours:")
        if guess != correct_guess_string:
            pass








