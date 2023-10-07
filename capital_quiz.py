import random
import json

game_status = None
questions_done = 0
stop_game = None


with open('list.txt', 'r') as file:
    dictionary = json.load(file)

def list_shuffle():
    shuffling_items = list(dictionary.items())
    random.shuffle(shuffling_items)
    shuffled_dict = dict(shuffling_items)
    return shuffled_dict

def game_mode():
    while True:
        mode_select = input("Welcome to the quiz! Select either easy (with hints) or hard mode (without hints). To continue type 'easy' or 'hard': ").strip().lower()
        if mode_select == "easy":
            game_easy()
            break
        elif mode_select == "hard":
            game_hard()
            break
        else:
            print("Type 'easy' or 'hard' to continue")


def game_easy():
    shuffled_dict = list_shuffle()
    questions_total = len(shuffled_dict)
    points_total = 0 #amount of question
    points_gotten = 0 #amount of questions answered right
    global game_status
    global stop_game
    global questions_done
    while game_status != "finished":
        for country, capital in shuffled_dict.items():
            if stop_game == "yes":
                break
            lifes = 3
            questions_done += 1
            points_total = questions_done
            hints = 0
            answer = input(f"[{questions_done}/{questions_total}] What's the capital of {country}? HINT: {capital[hints]} (type 'stop' to quit): ").strip()
            lifes -= 1
            if answer.lower() == "stop":
                break
            elif answer.lower() != capital.lower():
                hints += 1
                while True:
                    hints += 1
                    if lifes == 1:
                        print(f"Wrong! You have {lifes} guess left.")
                        answer = input(f"What's the capital of {country}? HINT: {capital[:hints]} (type 'stop' to quit):  ").strip()
                        lifes -= 1
                        if answer.lower() == capital.lower():
                            print("\n")
                            print(f"Correct answer! Capital of {country} is indeed {capital}.")
                            print("\n")
                            points_gotten += 1
                            break
                        elif answer.lower() == "stop":
                            stop_game = "yes"
                            break
                        elif lifes == 0:
                            print("\n")
                            print(f"Wrong! Capital of {country} is {capital}. Moving on to the next question.")
                            print("\n")
                            break
                    else:
                        print(f"Wrong! You have {lifes} guesses left.")
                        answer = input(f"What's the capital of {country}? HINT: {capital[:hints]} (type 'stop' to quit):  ").strip()
                        lifes -= 1
                        if answer.lower() == capital.lower():
                            print("\n")
                            print(f"Correct answer! Capital of {country} is indeed {capital}.")
                            print("\n")
                            points_gotten += 1
                            break
                        elif answer.lower() == "stop":
                            stop_game = "yes"
                            break
                        elif lifes == 0:
                            print("\n")
                            print(f"Wrong! Capital of {country} is {capital}. Moving on to the next question.")
                            print("\n")
                            break
            else:
                print("\n")
                print(f"Correct answer! Capital of {country} is indeed {capital}.")
                print("\n")
                points_gotten += 1
        game_status = "finished"
    if points_total == 1:
        print(f"Quiz finished! You got {points_gotten} right out of {points_total} question.")
    else:
        print(f"Quiz finished! You got {points_gotten} right out of {points_total} questions.")

def game_hard():
    shuffled_dict = list_shuffle()
    questions_total = len(shuffled_dict)
    points_total = 0 #amount of question
    points_gotten = 0 #amount of questions answered right
    global game_status
    global stop_game
    global questions_done
    while game_status != "finished":
        for country, capital in shuffled_dict.items():
            if stop_game == "yes":
                break
            lifes = 3
            questions_done += 1
            points_total = questions_done
            answer = input(f"[{questions_done}/{questions_total}] What's the capital of {country}? (type 'stop' to quit): ").strip()
            lifes -= 1
            if answer.lower() == "stop":
                break
            elif answer.lower() != capital.lower():
                while True:
                    if lifes == 1:
                        print(f"Wrong! You have {lifes} guess left.")
                        answer = input(f"What's the capital of {country}? (type 'stop' to quit):  ").strip()
                        lifes -= 1
                        if answer.lower() == capital.lower():
                            print("\n")
                            print(f"Correct answer! Capital of {country} is indeed {capital}.")
                            print("\n")
                            points_gotten += 1
                            break
                        elif answer.lower() == "stop":
                            stop_game = "yes"
                            break
                        elif lifes == 0:
                            print("\n")
                            print(f"Wrong! Capital of {country} is {capital}. Moving on to the next question.")
                            print("\n")
                            break
                    else:
                        print(f"Wrong! You have {lifes} guesses left.")
                        answer = input(f"What's the capital of {country}? (type 'stop' to quit):  ").strip()
                        lifes -= 1
                        if answer.lower() == capital.lower():
                            print("\n")
                            print(f"Correct answer! Capital of {country} is indeed {capital}.")
                            print("\n")
                            points_gotten += 1
                            break
                        elif answer.lower() == "stop":
                            stop_game = "yes"
                            break
                        elif lifes == 0:
                            print("\n")
                            print(f"Wrong! Capital of {country} is {capital}. Moving on to the next question.")
                            print("\n")
                            break
            else:
                print("\n")
                print(f"Correct answer! Capital of {country} is indeed {capital}.")
                print("\n")
                points_gotten += 1
        game_status = "finished"
    if points_total == 1:
        print(f"Quiz finished! You got {points_gotten} right out of {points_total} question.")
    else:
        print(f"Quiz finished! You got {points_gotten} right out of {points_total} questions.")

if __name__ == "__main__":
    game_mode()
