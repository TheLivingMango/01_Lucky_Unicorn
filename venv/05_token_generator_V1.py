import random

tokens = ["unicorn", "horse", "zebra", "donkey"]
chosen = random.choice(tokens)
print(chosen)
for item in range(0,20):
    chosen = random.choice(tokens)
    print(chosen, end=' t ')
