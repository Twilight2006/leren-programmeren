stickernames = {'rudi' , 'arnold' , 'jeroen' , 'kjeld'}

leeftijd = input(' wat is uw leeftijd?: ')
leeftijd = int(leeftijd)

if leeftijd > 17:
    print(' kom maar naar binnen')
    name = input(' wat is uw naam? ')
    bandje = False

    if leeftijd >= 21:
        print('u krijgt een bandje ')
        bandje = True
    elif name in {'rudi' , 'arnold' , 'jeroen' , 'kjeld'}:
        print('u krijgt een sticker ')

    drink = input(' wat wil je drinken? A, Bier of B, cola ')

    if drink == 'A':
        if bandje == False and drink == 'A':
            print(' sorry, dat mag je niet bestellen')
    else:
        print(' dit kost 1,50 euro ')
elif drink == 'B':
    if stickernames == True:
        print(' die is gratis voor u ')
    else:
        print(' dit kost 1,00 euro ')
    
else:
    print(' u mag niet naar binnen ')




















