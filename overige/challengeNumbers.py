kleinste = 1000
grootste = 0
deelbaar = 0

for x in range(20):
    vraag = int(input('getal? '))

    if vraag < kleinste:
        kleinste = vraag

    if vraag > grootste:
        grootste = vraag
    
    if vraag % 3 == 0:
        deelbaar+=1

print(f'Kleinste: {kleinste}')
print(f'Grootste: {grootste}')
print(f'Deelbaar: {deelbaar}')







