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
    played_before = yes_no("Have you played this game before")
    print("You chose {}".format(played_before))
    if played_before == "no":
        instructions()
    print("Program continues")

def how_much(question):
    error = "Please enter a whole number between 1 and 10\n"
valid = False
while not valid:
    try:

        response = int(input("How much would you"
                             " like to play with?"))

        if 0 > response <=10:

            print("You have asked to play"
              " with ${}".format(response))

        else:
            print(error)
    except ValueError:
            print(error)
