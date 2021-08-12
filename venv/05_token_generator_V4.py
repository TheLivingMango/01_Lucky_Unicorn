import random

STARTING_BALANCE = 100

balance = STARTING_BALANCE

chosen = random.choice(tokens)
print(chosen)
for item in range(0, 500):
    chosen_num = random.randint(1, 100)

    print(chosen, end=' \t ')

    if 1 <= chosen_num <= 5:
            chosen = "unicorn":
        balance += 4

elif 6<= chosen_num <= 36:
    chosen = "donkey":
        balance -= 1

    else:
        chosen = "horse / zebra"
        balance -= 0.5

    print("Starting Balance ${:.2f}".format(STARTING_BALANCE))
    print("Final Balance ${:.2f}".format(balance))
