crois = input('hoeveel croisantjes wilt u?: ')
prijscrois = int(crois) * 0.39
print(prijscrois)

stok = input('hoeveel stokbroden wilt u? : ')
prijsstok = int(stok) * 2.78
print(prijsstok)

korting = input('heeft u nog kortingbonnen? : ')
totalekorting =  int(korting) * 0.50
print(totalekorting)

totaalprijs = prijscrois + prijsstok - totalekorting

print(' u moet ' + str(totaalprijs) + ' betalen ')
