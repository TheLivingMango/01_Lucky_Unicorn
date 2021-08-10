import random

tokens = ["unicorn", "horse", "zebra", "donkey"]
balence = 100

print(chosen)
for item in range(0,20):
    chosen = random.choice(tokens)
    print(chosen, end=' t ')

    if chosen == "unicorn":
        balence +=4

    elif chosen == "donkey":
        balence -1

    else :
        balence -0.5

        print("Token : {}, Balence: ${}".format(chosen, balence))
