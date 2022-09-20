person = input(' met hoeveel personen zijn jullie? : ')
persons = int(person) * 7.45
print(persons)

vip =  input(' hoeveel minuten wilt u in de vip-VRgameseat? : ')
viptijd = int(vip) / 5 * 0.37
print(viptijd)

totaalprijs = viptijd + persons

print( 'u moet ' +  str(totaalprijs) + ' betalen ')



