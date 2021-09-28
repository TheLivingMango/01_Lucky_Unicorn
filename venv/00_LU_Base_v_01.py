# Imports
import random
# Functions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please answer yes / no")


def instructions():
    print("****How to Play****")
    print()
    print("The rules of the game go here")
    print()
    return ""


def number_check(question):
    error = "Please enter a whole number between 1 and 10"
    valid = False
    while not valid:
        try:
            response = int(input(question))

            if 0 < response <=10:
                print("You have asked to play with ${}".format(response))
                return response

            else:
                print(error)
        except ValueError:
            print(error)



# *** Main Routine ***
rounds_played = 0
balance = 0

played_before = yes_no("Have you played this game before")
if played_before == "no":
    instructions()

how_much = number_check("How much do you want to play with? ")
balance = how_much

play_again = input("Press <Enter> to play...")
while play_again == "":

    rounds_played += 1
    print("***Round #{}***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
            balance -= 0.5
        else:
            chosen = "zebra"
            balance -= 0.5

    print("You got {}".format(chosen))
    print("Balance {}".format(balance))

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")

    else:
        play_again = input("Press <Enter> to play again"
                           " or 'xxx' to quit")

print()
print("Final Balance:", balance)
