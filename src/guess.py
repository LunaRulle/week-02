import random

first_time = True
def yes_or_no(answer):
    if answer == "y":
        return True
    else:
        return False

def user_input():
    while True:
        try:
            usr_input = int(input())
        except ValueError:
            print("Please write an intager")
            continue
        else:
            break
    return usr_input

def guessing_game(number_to_guess):
    global first_time
    guesses = 1
    while True:
        
        if guesses > 10:
            print("You ran out of guesses")
            guesses = 0
            first_time = False
            break
        else:
            pass

        usr_guess = user_input()
        if usr_guess == number_to_guess:
            print(f"Congratualtions you guessed the number {number_to_guess} correctly")
            print(f"you guessed {guesses} times")
            guesses = 0
            first_time = False
            break
        elif usr_guess > number_to_guess:
            print("The number you guessed is too big")
            guesses += 1
            continue
        elif usr_guess < number_to_guess:
            print("The number you guessed is too small")
            guesses += 1
            continue
    return first_time

while True:
    number_to_guess = random.randrange(1, 100, 1)
    if first_time == True:
        print("Please guess a number for 1 to 100")
        guessing_game(number_to_guess)
    else:
        answer = yes_or_no(input("Would you like to play again? (y/n) "))
        if answer == True:
            print("Guess the number")
            guessing_game(number_to_guess)
        else:
            print("Thank you for playing!")
            exit()
