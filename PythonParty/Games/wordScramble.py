from random import random, randint, shuffle

from Games import helper_Functions
def word_game(engine,tts):
    word1 = ["germany","light","cone","earth","line","magnificent","nice","oxygen","juice","photosynthesis"
             ,"plant","consumer","yellow","carrot","lettuce","laptop","mouse","cheetah","eagle",
             "canada","vietnam","road","plague","flag","christmas","wire","wild","ancient","jungle",
             "forest","mail","cloud","highway","hypnotize","tractor","wizard","bungalow","condition","criminal",
             "monkey","snow", "cedar", "pokemon", "smart","intelligent","aircraft","shoe","turbine","dear"
             ,"turquoise","jacket","roof","stone","maple", "syrup","brick"]

    s1 = "Welcome to word scramble! Each team nominate a team captain!"
    s2 = "A scrambled word will be displayed and the teams will race to decoding it."
    s3 = "Once a team figures out the word they should whisper it to the team captain."
    s4 = "The team captain will sit near the laptop and type the unscrambled word into the computer."
    s5 = "The first team to get to 5 correct unscrambles wins."

    helper_Functions.pntSpeak(engine, tts, s1)
    helper_Functions.pntSpeak(engine, tts, s2)
    helper_Functions.pntSpeak(engine, tts, s3)
    helper_Functions.pntSpeak(engine, tts, s4)
    helper_Functions.pntSpeak(engine, tts, s5)
    input("Press enter to start: ")

    while True:
        rnd_val = randint(0,len(word1)-1)
        scmble = shuffle(word1[rnd_val])
        print(scmble)
        input("")