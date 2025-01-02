from random import randint, random, choice
import keyboard
import pyautogui

from Games import helper_Functions

def obj_game(eng, tts, team1, team2):
    take_in = "abcd1234"
    team1Points = 0
    team2Points = 0
    pressed = True
    game_start = False
    rnd_start = True
    usedVals = []

    s1 = "Welcome to object retrival. In this game the goal is to retrieve the objects."
    s2 = "One player from each team will be selected. An object will be selected."
    s3 = "The first player to get the object, bring it to the computer, and press their respective teams key, "
    s4 = "'F' for team 1 and 'J' for team 2 win the point."
    s5 = "First team to 5 objects wins."
    fnd_lst = ("a left Shoe", "a bottle of water", "a shampoo bottle", "a toliet paper", "something wooden", "something hard",
    "something that tells time", "something that has legs", "something that smells", "a rock", "something made of metal",
    "something tasty", "something sweet", "a small friend")
    pyautogui.hotkey('ctrl', 'l')
    helper_Functions.pntSpeak(eng, tts, s1)
    helper_Functions.pntSpeak(eng, tts, s2)
    helper_Functions.pntSpeak(eng, tts, s3)
    helper_Functions.pntSpeak(eng, tts, s4)
    helper_Functions.pntSpeak(eng, tts, s5)
    if take_in != input("Ready? Press enter to start: "):
        game_start = True
    while game_start:
        if rnd_start:
            rnVal = randint(0, len(fnd_lst) - 1)
            while rnVal in usedVals:
                rnVal = randint(0, len(fnd_lst) - 1)
            helper_Functions.pntSpeak(eng, tts, f"\n{choice(team1)} and {choice(team2)} find {fnd_lst[rnVal]}")
            usedVals.append(rnVal)
        rnd_start = False
        if keyboard.is_pressed("f") and pressed:
            pressed = False
            team1Points += 1
            rnd_start = True
            helper_Functions.pntSpeak(eng, tts, f"Team 1 got the point! Team 1 now has {team1Points} and team 2 now has {team2Points}")
        if keyboard.is_pressed("j") and pressed:
            pressed = False
            team2Points += 1
            rnd_start = True
            helper_Functions.pntSpeak(eng, tts, f"Team 2 got the point! Team 1 now has {team1Points} and team 2 now has {team2Points}")
        if team1Points > 4 or team2Points > 4:
            break
        if not pressed:
            helper_Functions.pntSpeak(eng, tts, "Press enter for the next round!")
            input(">")
            pressed = True
            rnd_start = True

    if team1Points > team2Points:
        helper_Functions.pntSpeak(eng, tts, "\nTeam 1 won this mini game!")
        input("Press enter to continue to the next game")
        return 1
    else:
        helper_Functions.pntSpeak(eng, tts, "\nTeam 2 won this mini game!")
        input("Press enter to continue to the next game")
        return 2