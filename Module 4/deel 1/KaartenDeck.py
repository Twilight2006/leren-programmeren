import random
nummers = [2,3,4,5,6,7,8,9,10, "Boer", "Vrouw", "Heer", "Aas"]
joker = 2
kleuren = ["Harten", "Klaveren", "Schoppen", "Ruiten"]
deck = []

for i in range(len(kleuren)):
    for j in range(len(nummers)):
        deck.append(f"{kleuren[i]} {nummers[j]}")

kaartnummer = 1
for i in range (7):
    random.shuffle(deck)
    print(f"Kaart {kaartnummer}; {deck.pop(0)}")
    kaartnummer = kaartnummer + 1
print("")
print(f"deck (47 kaarten): {deck}")



