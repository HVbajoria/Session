import random

def ask_riddle():
    riddles = [
        "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        "What has keys but can't open locks?",
        "What has a heart that doesn't beat?",
        "What has a face that doesn't smile?"
    ]
    answers = [
        "echo",
        "piano",
        "artichoke",
        "clock"
    ]
    sarcastic_responses = [
        "Oh, you're so close! Not.",
        "Nice try, but nope!",
        "Haha, wrong answer!",
        "You must be joking, right?"
    ]

    riddle_index = random.randint(0, len(riddles) - 1)
    riddle = riddles[riddle_index]
    answer = answers[riddle_index]
    sarcastic_response = sarcastic_responses[riddle_index]

    print(riddle)
    user_answer = input("Your answer: ")

    if user_answer.lower() == answer:
        print("Congratulations! You got it right!")
    else:
        print(sarcastic_response)

ask_riddle()