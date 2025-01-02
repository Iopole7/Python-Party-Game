from random import random, randint, shuffle

import pyautogui

from Games import helper_Functions


def word_game(engine,tts):
    word1 = ["germany","light","cone","earth","line","magnificent","nice","oxygen","juice","photosynthesis"
             ,"plant","consumer","yellow","carrot","lettuce","laptop","mouse","cheetah","eagle",
             "canada","vietnam","road","plague","flag","christmas","wire","wild","ancient","jungle",
             "forest","mail","cloud","highway","hypnotize","tractor","wizard","bungalow","condition","criminal",
             "monkey","snow", "cedar", "pokemon", "smart","intelligent","aircraft","shoe","turbine","dear"
             ,"turquoise","jacket","roof","stone","maple", "syrup","brick"]

    points_to_win = 5
    given_word = ""
    team1_points = 0
    team2_points = 0

    s1 = "Welcome to word scramble! Each team nominate a team captain!"
    s2 = "A scrambled word will be displayed and the teams will race to decoding it."
    s3 = "Once a team figures out the word they should whisper it to the team captain."
    s4 = "The team captain will sit near the laptop and type the unscrambled word into the computer."
    s5 = "The first team to get to 5 correct unscrambles wins."
    pyautogui.hotkey('ctrl', 'l')
    helper_Functions.pntSpeak(engine, tts, s1)
    helper_Functions.pntSpeak(engine, tts, s2)
    helper_Functions.pntSpeak(engine, tts, s3)
    helper_Functions.pntSpeak(engine, tts, s4)
    helper_Functions.pntSpeak(engine, tts, s5)
    input("Press enter to start: ")

    while True:
        given_word = ""
        rnd_val = randint(0,len(word1)-1)
        correct_word = word1[rnd_val]
        scramble_word = list(word1[rnd_val])
        shuffle(scramble_word)
        scramble_string = ''.join(scramble_word)
        helper_Functions.pntSpeak(engine, tts, f"Unscramble {scramble_string}")
        while given_word != correct_word:
            given_word = input("Enter the word: ")
            if given_word.lower() == "skip":
                print(f"The correct word is: {correct_word}")
                break
        if given_word.lower() == "skip":
            continue
        helper_Functions.pntSpeak(engine, tts, f"Correct! Which team got the point '1' or '2'?")
        correct_team = input(">")
        if correct_team == "1":
            team1_points += 1
        else:
            team2_points += 1
        helper_Functions.pntSpeak(engine, tts, f"Team 1 has {team1_points}. Team 2 has {team2_points}")
        if team1_points >= 5:
            return 1
        elif team2_points >= 5:
            return 2