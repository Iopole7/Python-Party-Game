from random import randint
from time import sleep

from Games import helper_Functions
import pygame
def mem_game(engine, tts):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    running = True
    colours = ("g", "r", "b", "y")
    correct_guess = []
    correct_guess_string = ''.join(map(str, correct_guess))
    guess = ""
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
        for val in correct_guess:
            if val == "g":
                screen.fill("green")
                pygame.display.flip()
            elif val == "r":
                screen.fill("red")
                pygame.display.flip()
            elif val == "b":
                screen.fill("blue")
                pygame.display.flip()
            elif val == "y":
                screen.fill("yellow")
                pygame.display.flip()
            sleep(0.5)
        guess = input("Colours:")
        if guess != correct_guess_string:
            break

    pygame.quit()





