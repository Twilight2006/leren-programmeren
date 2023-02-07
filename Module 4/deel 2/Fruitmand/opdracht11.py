from fruitmand import fruitmand

verder = True

mandkleur = []
for i in range(len(fruitmand)):
    mandkleur.append(fruitmand[i]["color"])

del mandkleur[3]
del mandkleur[4]

for k in mandkleur:
    print(k)

while verder == True:
    kleur = input("Please enter color here: ").lower()
    if kleur in mandkleur:
        print("f")
        verder = False
    else:
        print("Sorry, nothing in the basket has that color.")