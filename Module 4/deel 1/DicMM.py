import random

kleuren = ["rood", "groen", "geel", "bruin", "blauw"]
zakMM = {
    "rood": 0,
    "groen": 0,
    "geel": 0,
    "bruin":0,
    "blauw": 0
}

erbij = int(input("Hoeveel M&M's wilt u toevoegen? : "))
for i in range(erbij):
    gekozen = random.choice(kleuren)
    zakMM[gekozen]+=1

print(zakMM)



