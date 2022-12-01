# name of student: Sven van den Heuvel
# number of student: 99072042
# purpose of program: wisselgeld berekenen
# function of program:
# structure of program:
  
paid500 = 0
paid200 = 0
paid100 = 0
paid50 = 0
paid20 = 0
paid10 = 0
paid5 = 0
paid2 = 0
paid1 = 0

toPay = int(float(input('Amount to pay: '))* 100) # 'topay' is een float(kommagetal) 'amount to pay' * 100
paid = int(float(input('Paid amount: ')) * 100) # hetzelfde als de vorige, maar dan voor paid amount
change = paid - toPay # 'change' paid - topay(floats)

if change > 0: # als de 'change' hoger is dan 0, 
  coinValue = 500 # wordt de 'coinvalue' 500
  
  while change > 0 and coinValue > 0: # wanneer de 'change' en de 'coinvalue' groter is dan 0,
    nrCoins = change // coinValue # 'nrcoins' is change:coinvalue

    if nrCoins > 0: # als 'nrcoins' groter is dan 0, print hij de volgende code:
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #+


# comment on code below: de coinvalue is in centen, dus bv: 100 cent = 1 euro. dus: coinvalue = 100
    if coinValue == 500:
      paid500 = nrCoinsReturned
      coinValue = 200  
    elif coinValue == 200:
      paid200 = nrCoinsReturned
      coinValue = 100
    elif coinValue == 100:
      paid100 = nrCoinsReturned
      coinValue = 50 
    elif coinValue == 50:
      paid50 = nrCoinsReturned
      coinValue = 20    
    elif coinValue == 20:
      paid20 = nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      paid10 = nrCoinsReturned
      coinValue = 5 
    elif coinValue == 5:
      paid5 = nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      paid2 = nrCoinsReturned
      coinValue = 1
      paid1 = nrCoinsReturned
    else:
      coinValue = 0


if change > 0: # als de 'change' groter is dan 0, dan print het programma dat het niks teruggeeft.
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')

kassabon = [paid500, paid200, paid100, paid50, paid20, paid10, paid5, paid2, paid1]
for paid in kassabon:
  print(paid, "keer teruggegeven")
