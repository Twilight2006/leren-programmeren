#Sven van den Heuvel : pizzacalculator

prijssmall = 3.99
prijsmedium = 6.99
prijslarge = 10.99


print('Welkom bij de pizzaria!')
print('kijk naar de lijst, welke pizza wilt u? ')
print('small : 3,99 per/stuk')
print('medium : 6,99 per/stuk')
print('large : 10,99 per/stuk')

totaalsmall = input('hoeveel maat ''small'' wilt u bestellen? ')
totaalsma = int(totaalsmall) * 3.99
print( ' dat wordt ' + str(totaalsma) + ' voor ' + totaalsmall + ' small pizza(s) ')

totaalmedium = input('hoeveel maat ''medium'' wilt u bestellen? ')
totaalmed = int(totaalmedium) * 6.99
print( ' dat wordt ' + str(totaalmed) + ' voor ' + totaalmedium + ' medium pizza(s) ' )

totaallarge = input('hoeveel maat ''large'' wilt u bestellen? ')
totaallar = int(totaallarge) * 10.99
print( ' dat wordt ' + str(totaallar) + ' voor ' + totaallarge + ' large pizza(s) ')

totaalprijs = totaalsma + totaalmed + totaallar

print(' day wordt dan ' + str(totaalprijs) + ' euro alstublieft ')

print(' hier heeft u nog het bonnetje ')
print('------------------------------------')
print(' aantal small: ' + str(totaalsmall))
print(' aantal medium: ' + str(totaalmedium))
print(' aantal large: ' + str(totaallarge))
print(' totaalprijs: ' + str(totaalprijs))
print('------------------------------------')

