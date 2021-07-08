def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            return response
        response = "no"
        return response

    else:
        print("please choose Yes or No")

    response = yes_no("Have you played this game before?")
    return response
    print("You chose {}".fomat(show_instructions))

    response = input("Have you played this game before?").lower()
    return response
    if response == "yes" or response == "y":
        print("program Continues")


    elif response == "no" or response == "n":
            return response
                print("display instructions")

    else:
        print("Please answer with y / n")
