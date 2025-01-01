from Games import helper_Functions

s1 = "Welcome to trivia! Please select the categories:"

hist = [
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
]
geo = [{
        "question": "What is the A in sir John A. Mcdonald?",
        "choices": {"a":"Alexander","b":"Alexsis","c":"Alton", "d":"Adam"},
        "answer": "a"
    },]
misc = [{
        "question": "What is the A in sir John A. Mcdonald?",
        "choices": {"a":"Alexander","b":"Alexsis","c":"Alton", "d":"Adam"},
        "answer": "a"
    },]

def trivia_game(eng,tts):
    helper_Functions.pntSpeak(eng, tts, s1)