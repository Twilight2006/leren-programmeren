import random

kleuren = ["Oranje", "Blauw", "Groen", "Bruin"]
indezak = []
erbij = int(input("Hoeveel M&M's wilt u toevoegen aan de zak?: "))
for i in range(erbij):
    color = random.choice(kleuren)
    indezak.append(color)

print(indezak)



