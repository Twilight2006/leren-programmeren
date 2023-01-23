from fruitmand import fruitmand
import random

fruit = random.choice(fruitmand)

x = int(input("Vul een nummer in: "))
for i in range(x):
    print(fruit["name"])



