from fruitmand import fruitmand

numlist = []

for i in range(len(fruitmand)):
    numlist.append(fruitmand[i]["weight"])
    numlist.sort(reverse=True)

print(numlist)



