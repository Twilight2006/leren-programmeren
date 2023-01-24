from fruitmand import fruitmand
import random

x = int(input("vul een getal in: "))
for i in range(x):
    fruit = random.choice(fruitmand)
    print(fruit["name"])
