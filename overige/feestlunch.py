<<<<<<< HEAD
crois = input('hoeveel croisantjes wilt u?: ')
prijscrois = int(crois) * 0.39
print(prijscrois)

stok = input('hoeveel stokbroden wilt u? : ')
prijsstok = int(stok) * 2.78
print(prijsstok)

korting = input('heeft u nog kortingbonnen? : ')
totalekorting =  int(korting) * 0.50
print(totalekorting)

print(prijscrois + prijsstok - totalekorting)
=======
print('De feestlunch kost je bij de bakker 10.69 voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')

cro = 17
prijs = 0.39
sto = 2
prijs2 = 2.78
korting = 0.50
aantal = 3

totaal = cro * prijs

print(totaal)

totaal2 = sto * prijs2

print(totaal2)

totaal3 = korting * aantal

print(totaal3)

totaalprijs = totaal + totaal2 - totaal3

print(totaalprijs)
>>>>>>> 80d2f58b4642ef43c2ed1e4f8e177c5d5755861a
