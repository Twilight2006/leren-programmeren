from fruitmand import fruitmand

fruitlist = []

meloen = {
    'name' : 'watermeloen',
    'weight' : 375,
    'color' : 'pink',
    'round' : True
}

fruitmand.append(meloen)

for i in range(len(fruitmand)):
    fruitlist.append(fruitmand[i]["weight"])

print(fruitlist)

print(sum(fruitlist))








