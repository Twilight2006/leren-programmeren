from fruitmand import fruitmand

reversedlist = []

for i in range(len(fruitmand)):
    reversedlist.append(fruitmand[i]['name'])
fruit = list(reversed(reversedlist))

for f in fruit:
    print(f)