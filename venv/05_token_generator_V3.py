import random

tokens = ["unicorn", "horse", "horse", "horse",
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE

chosen = random.choice(tokens)
print(chosen)
for item in range(0, 20):

    print(chosen, end=' \t ')

    if chosen == "unicorn":
        balance += 4

    elif chosen == "donkey":
        balance -= 1

    else:
        balance -= 0.5

    print("Starting Balance ${:.2f}".format(STARTING_BALANCE))
    print("Final Balance ${:.2f}".format(balance))
