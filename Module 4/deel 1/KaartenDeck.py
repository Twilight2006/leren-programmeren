import random
nummers = [2,3,4,5,6,7,8,9,10, "Boer", "Vrouw", "Heer", "Aas"]
joker = 2
kleuren = ["Harten", "Klaveren", "Schoppen", "Ruiten"]
deck = []

for i in range(len(kleuren)):
    for j in range(len(nummers)):
        deck.append(f"{kleuren[i]} {nummers[j]}")

for i in range (1,8):
    random.shuffle(deck)
    print(f"Kaart {i}; {deck.pop(0)}")

print("")
print(f"deck (47 kaarten): {deck}")



