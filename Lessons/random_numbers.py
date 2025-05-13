# Hay que importar random para utilizarlo, elige aleatoriamente entre lo que le indiques.
import random

low = 0
high = 100
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
options = ("rock", "paper", "scissors")

# print(random.randint(1, 10))
# print(random.choice(options))
# print(random.randint(low, high))

random.shuffle(cards)
for i in cards:
    print(i, end=" ")

