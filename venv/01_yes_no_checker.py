show_instructions = input("Have you played this game before?").lower()

if show_instructions == "yes":
    print("program Continues")

elif show_instructions == "y":
    print("program continues")

elif show_instructions == "no":
    print("display instructions")

elif show_instructions == "n":
    print("display instructions")

else:
    print("Please answer with y / n")
