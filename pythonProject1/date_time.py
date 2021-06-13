import datetime
import random


def show_date():
    print(datetime.datetime.today())


def guess_the_number():
    counter = 0
    chance = 10
    guessNumber = random.randint(1, 10)
    while counter < chance:
        userGuess = int(input("Enter guess number:"))
        if userGuess == guessNumber:
            print("Congratulations, You guessed the number")
            break
        elif userGuess > guessNumber:
            print("Too high")
        elif userGuess < guessNumber:
            print("Too Low")


print("Today's date and time is ")
show_date()
guess_the_number()
