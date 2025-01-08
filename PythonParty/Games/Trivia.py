from random import random, randint

import pyautogui

from Games import helper_Functions

point_to_win = 7
s1 = "Welcome to trivia! Each team will be given the chance to discuss and input a guess!"
s2 = f"The team that reaches {point_to_win} points first wins!"
s3 = "Team 1 please enter your guess: "

question = [
    {
        "question": "What is the A in sir John A. Mcdonald?",
        "choices": {"a":"Alexander","b":"Alexsis","c":"Alton", "d":"Adam"},
        "answer": "a"
    },
    {
        "question": "What year was the current Canadian flag adopted?",
        "choices": {"a":"1952","b":"1941","c":"1965", "d":"1936"},
        "answer": "c"
    },
    {
        "question": "Which artist painted the ceiling of the Sistine Chapel?",
        "choices": {"a":"Leonardo da Vinci","b":"Leonardo DiCaprio","c":"Michelangelo di Lodovico Buonarroti Simoni", "d":"Raffaello Sanzio da Urbino"},
        "answer": "c"
    },
    {
        "question": "Who is on the $5 Canadian bill?",
        "choices": {"a":"John Mcdonald","b":"Wilfred Laurier","c":"Mackenzie king", "d":"Pierre Elliot Trudeau"},
        "answer": "b"
    },
    {
        "question": "What did William the Conqueror conquer?",
        "choices": {"a":"Normandy","b":"England","c":"Ireland", "d":"Russia"},
        "answer": "b"
    },
    {
        "question": "What year was the American revolution?",
        "choices": {"a":"1775","b":"1792","c":"1877", "d":"1752"},
        "answer": "a"
    },
    {
        "question": "When was the fall of the western Roman Empire?",
        "choices": {"a":"221","b":"476","c":"1021", "d":"2019"},
        "answer": "b"
    },
    {
        "question": "Who was the leader of Germany in WW1?",
        "choices": {"a":"Hitler","b":"Charles IIV","c":"Louis II", "d":"Wilhelm II"},
        "answer": "d"
    },
    {
        "question": "What is the largest contiguous empire in history?",
        "choices": {"a":"Mongol Empire","b":"British Empire","c":"French Empire", "d":"Russian Empire"},
        "answer": "a"
    },
    {
        "question": "Where did Albert Einstein live before moving to the United States?",
        "choices": {"a":"France","b":"Scotland","c":"China", "d":"Germany"},
        "answer": "d"
    },
    {
        "question": "Who was the first person in the world to land on the moon?",
        "choices": {"a":"Neil deGrasse Tyson","b":"Buzz Aldrin","c":"Neil Armstrong", "d":"Franz Hotlzmahn"},
        "answer": "c"
    },
    {
        "question": "Who was the first Emperor of Rome?",
        "choices": {"a":"Augustus","b":"Caesar","c":"Valentino", "d":"Tiberius"},
        "answer": "a"
    },
    {
        "question": "Which Greek goddess was the Parthenon dedicated to?",
        "choices": {"a":"Hestia","b":"Hera","c":"Athena", "d":"Artemis"},
        "answer": "c"
    },
    {
        "question": "Ivan the Terrible was the leader of which empire?",
        "choices": {"a":"Nepal","b":"Poland","c":"Russia", "d":"Persia"},
        "answer": "c"
    },
    {
        "question": "What is the largest organism on Earth by dry weight(With the water removed)",
        "choices": {"a":"Mushroom","b":"Tree","c":"Whale", "d":"Your mother"},
        "answer": "b"
    },
    {
        "question": "Where is cinnamon native to?",
        "choices": {"a":"South Asia","b":"East Asia","c":"Africa", "d":"South America"},
        "answer": "a"
    },
    {
        "question": "Where are potatoes native to?",
        "choices": {"a":"South America","b":"North America","c":"Europe", "d":"Australia"},
        "answer": "a"
    },
    {
        "question": "Where is sugar cane native to?",
        "choices": {"a":"Sudan","b":"New Guinea","c":"Equatorial Guinea", "d":"Old Guinea"},
        "answer": "b"
    },
    {
        "question": "What large mammal is responsible for the most human deaths in Africa?",
        "choices": {"a":"Lion","b":"Elephant","c":"Tiger", "d":"Hippo"},
        "answer": "d"
    },
    {
        "question": "Approximately how many people each year die to coconuts?",
        "choices": {"a":"0-50","b":"51-100","c":"101-150", "d":"151+"},
        "answer": "d"
    },
    {
        "question": "Which planet has the largest moon?",
        "choices": {"a":"Earth","b":"Jupiter","c":"Saturn", "d":"Uranus"},
        "answer": "b"
    },
    {
        "question": "Which moon is larger than Mercury?",
        "choices": {"a":"Moon(Earth)","b":"Io","c":"Titan", "d":"Europa"},
        "answer": "c"
    },
    {
        "question": "Rocks that are formed from cooled lava are called...",
        "choices": {"a":"Obsidian","b":"Metamorphic","c":"Igneous", "d":"Rigatory"},
        "answer": "c"
    },
    {
        "question": "Mount Everest is part of the ____ mountain range.",
        "choices": {"a":"Alpine","b":"Andes","c":"Himalayas", "d":"Chinese"},
        "answer": "c"
    },
    {
        "question": "The most abundant element in the atmosphere is...",
        "choices": {"a":"Oxygen","b":"Carbon","c":"Air", "d":"Nitrogen"},
        "answer": "d"
    },
    {
        "question": "The most abundant element in the Earth's crust is...",
        "choices": {"a":"Oxygen","b":"Aluminum","c":"Iron", "d":"Silicone"},
        "answer": "a"
    },
    {
        "question": "The inside part of modern American pennies is made of...",
        "choices": {"a":"Iron","b":"Nickel","c":"Copper", "d":"Zinc"},
        "answer": "d"
    },
    {
        "question": "The country with the most Muslims is...",
        "choices": {"a":"Pakistan","b":"Iran","c":"Saudi Arabia", "d":"Indonesia"},
        "answer": "d"
    },
    {
        "question": "What country has the most populated capital city (No metro area)?",
        "choices": {"a":"China","b":"India","c":"Japan", "d":"United States"},
        "answer": "a"
    },
    {
        "question": "1 millisecond is how many picoseoconds? ",
        "choices": {"a":"1e+3","b":"1e+6","c":"1e+9", "d":"1e+12"},
        "answer": "c"
    },
    {
        "question": "Rene Descartes is known for the development of...",
        "choices": {"a":"Cartwheel","b":"Cartesian Coordinates","c":"Decision Trees", "d":"French Fries"},
        "answer": "b"
    },
    {
        "question": "When was the first recorded indoor hockey match?",
        "choices": {"a":"1875","b":"1847","c":"1901", "d":"1892"},
        "answer": "a"
    },
    {
        "question": "Where was soccer invented?",
        "choices": {"a":"France","b":"Argentina","c":"Brazil", "d":"England"},
        "answer": "d"
    },
    {
        "question": "What was the average male height in victorian(late 18th century)?",
        "choices": {"a":"155-160cm","b":"161-165cm","c":"166-170cm", "d":"170+cm"},
        "answer": "c"
    },
    {
        "question": "Average life expectancy in Canada(2022):",
        "choices": {"a":"~80 years","b":"~81 years","c":"~82 years", "d":"~83 years"},
        "answer": "b"
    },
    {
        "question": "Average children per women in Japan(2022)",
        "choices": {"a":"1.29","b":"1.26","c":"1.13", "d":"1.34"},
        "answer": "b"
    },
    {
        "question": "What is the estimated South Korean population in 2050?",
        "choices": {"a":"47 million","b":"56 million","c":"42 million", "d":"50 million"},
        "answer": "a"
    },
    {
        "question": "What is the estimated South Korean population in 2050?",
        "choices": {"a":"47 million","b":"56 million","c":"42 million", "d":"50 million"},
        "answer": "a"
    },
    {
        "question": "What is the estimated South Korean population in 2050?",
        "choices": {"a":"47 million","b":"56 million","c":"42 million", "d":"50 million"},
        "answer": "a"
    },
    {
        "question": "Where are chicken native to?",
        "choices": {"a":"Asia","b":"Africa","c":"Europe", "d":"South America"},
        "answer": "a"
    },
    {
        "question": "Which one is a Madonna song",
        "choices": {"a":"Material Girl","b":"Lovin' You","c":"Wannabe", "d":"Iris"},
        "answer": "a"
    },
    {
        "question": "What do 2, 17, 29, and 31 have in common",
        "choices": {"a":"Nothing","b":"Odd","c":"Prime", "d":"Symmetric"},
        "answer": "c"
    },
    {
        "question": "What year was the first moon landing?",
        "choices": {"a":"1971","b":"1966","c":"1969", "d":"1962"},
        "answer": "c"
    },
    {
        "question": "What is a group of crows called?",
        "choices": {"a":"Frenzy","b":"Glant","c":"Murder", "d":"Posse"},
        "answer": "c"
    },
    {
        "question": "What is the symbol for potassium?",
        "choices": {"a":"P","b":"Po","c":"Pt", "d":"K"},
        "answer": "d"
    },
    {
        "question": "What does a sommelier specialize in?",
        "choices": {"a":"Smelling","b":"Wine","c":"Fruits", "d":"Trees"},
        "answer": "b"
    },
    {
        "question": "The southern tip of which continent is closest to Antarctica",
        "choices": {"a":"South America","b":"Africa","c":"Asia", "d":"Australia"},
        "answer": "a"
    },
    {
        "question": "Largest U.S state by population",
        "choices": {"a":"California","b":"Texas","c":"New York", "d":"Florida"},
        "answer": "a"
    },
    {
        "question": "Largest Canadian province by population",
        "choices": {"a":"Quebec","b":"Ontario","c":"Alberta", "d":"British Columbia"},
        "answer": "b"
    },
    {
        "question": "Largest Canadian province by population",
        "choices": {"a":"Quebec","b":"Ontario","c":"Alberta", "d":"British Columbia"},
        "answer": "b"
    },
    {
        "question": "Largest Canadian province by population",
        "choices": {"a":"Quebec","b":"Ontario","c":"Alberta", "d":"British Columbia"},
        "answer": "b"
    }
]

def trivia_game(eng,tts):
    counter = 0
    used_vals = []
    team1_points = 0
    team2_points = 0
    helper_Functions.pntSpeak(eng, tts, s1)
    helper_Functions.pntSpeak(eng, tts, s2)
    full_length = len(question)
    input("Press enter to start: ")
    while True:
        pyautogui.hotkey('ctrl', 'l')
        fact = randint(0, full_length - 1)
        while fact in used_vals:
            fact = randint(0,full_length-1)
            counter += 1
            if counter > 1500 and team1_points > team2_points:
                helper_Functions.pntSpeak(eng, tts, f"Ran out of questions! Team 1 won the mini game!")
                return 1
            elif counter > 1500 and team1_points < team2_points:
                helper_Functions.pntSpeak(eng, tts, f"Ran out of questions! Team 2 won the mini game!")
                return 2
            elif counter > 1500 and team1_points == team2_points:
                helper_Functions.pntSpeak(eng, tts, f"Ran out of questions! Tie!")
                return 0
        used_vals.append(fact)
        helper_Functions.pntSpeak(eng, tts,question[fact].get("question"))
        helper_Functions.pntSpeak(eng, tts, str(question[fact].get("choices")))
        helper_Functions.pntSpeak(eng, tts, s3)
        team1_guess = input(">")
        pyautogui.hotkey('ctrl', 'l')
        print(question[fact].get("question"))
        print(question[fact].get("choices"))
        team2_guess = input(">")
        answer = question[fact].get("answer")
        helper_Functions.pntSpeak(eng, tts, f"The answer is '{answer}'")
        if team1_guess == answer:
            team1_points += 1
            helper_Functions.pntSpeak(eng, tts, "Team 1 got a point!")
        else:
            helper_Functions.pntSpeak(eng, tts, "Team 1 did not get a point!")
        if team2_guess == answer:
            team2_points += 1
            helper_Functions.pntSpeak(eng, tts, "Team 2 got a point!")
        else:
            helper_Functions.pntSpeak(eng, tts, "Team 2 did not get a point!")
        helper_Functions.pntSpeak(eng, tts, f"Score: T1: {team1_points}, T2: {team2_points} ")
        if team1_points >= point_to_win and team1_points > team2_points:
            helper_Functions.pntSpeak(eng, tts, f"Team 1 won the mini game!")
            return 1
        if team2_points >= point_to_win and team2_points > team1_points:
            helper_Functions.pntSpeak(eng, tts, f"Team 2 won the mini game!")
            return 2
        input("Press enter to continue: ")
