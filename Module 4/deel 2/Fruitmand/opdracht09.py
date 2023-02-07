from fruitmand import fruitmand
totaal = []
kleuren = []

fruitmand.pop(4)

for i in range(len(fruitmand)):
    kleuren.append(fruitmand[i]["color"])
    print(kleuren)

del kleuren[3]
del kleuren[4]

for k in kleuren:
    print(k)

