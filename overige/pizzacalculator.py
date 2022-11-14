#Sven van den Heuvel : pizzacalculator

from platform import java_ver


prijssmall = 3.99
prijsmedium = 6.99
prijslarge = 10.99


print('Welkom bij de pizzaria!')
print('kijk naar de lijst, welke pizza wilt u? ')
print('small : 3,99 per/stuk')
print('medium : 6,99 per/stuk')
print('large : 10,99 per/stuk')

totaalsmall = input('hoeveel maat ''small'' wilt u bestellen? ')
totaals = int(totaalsmall) * 3.99
print( ' dat wordt ' + str(totaals) + ' voor ' + totaalsmall + ' small pizzas ')

totaalmedium = input('hoeveel maat ''medium'' wilt u bestellen? ')
totaalm = int(totaalmedium) * 6.99
print( ' dat wordt ' + str(totaalm) + ' voor ' + totaalmedium + ' medium pizzas ' )

totaallarge = input('hoeveel maat ''large'' wilt u bestellen? ')
totaall = int(totaallarge) * 10.99
print( ' dat wordt ' + str(totaall) + ' voor ' + totaallarge + ' large pizzas ')

totaalprijs = totaals + totaalm + totaall

print(' dat wordt dan ' + str(totaalprijs) + ' euro alstublieft ')

print('-----------------------------')
print(' small ' + str(totaalsmall))
print(' medium: ' + str(totaalmedium))
print(' large: ' + str(totaallarge))
print(' totaalprijs: ' + str(totaalprijs))
print('-----------------------------')










   










