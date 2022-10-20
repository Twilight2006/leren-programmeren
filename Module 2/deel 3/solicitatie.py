aangenomen = False
try:
    print(' hallo meneer/mevrouw, ' )
    print(' we gaan u een paar vragen stellen om te zien ')
    print(' ofdat u de verseiste ervaring heeft. ' )
    print(' op basis van uw antwoorden laten we u weten of u bent aangenomen.')
    name = input(' Wat is uw naam?: ')
    if name == 'sven':
        raise NameError('U mag niet dezelfde naam hebben als de eigenaar!')
    print(' Hallo, ' + name)
    dd = int(input(' hoeveel jaar ervaring heeft u met dieren-dressuur? : '))
    acrobatiek = int(input(' hoeveel jaar ervaring heeft u met acrobatiek? : '))
    jongleren = int(input(' hoeveel jaar ervaring heeft u met jongleren? : '))
    if dd > 3 or acrobatiek > 5 or jongleren > 2:
        aangenomen = True
    
    gender = input(' bent u een man of een vrouw? m/v: ')
    diploma = input(' heeft u een mbo-4 diploma ondernemen? ja/nee: ' )
    rijbewijs = input(' heeft u een geldig vrachtwagen rijbewijs? ja/nee: ')

    if diploma == 'nee' or rijbewijs == 'nee':
        aangenomen = False

    if gender == 'm':
        hoed = input(' heeft u een hoge hoed? ja/nee:')
        snor = input(' heeft u een snor? ja/nee: ')
        if snor == 'nee' and hoed == 'nee':
            aangenomen = False

        jsnor = int(input(' Hoe breed is uw snor in CM?: '))
        lengte = int(input(' Hoelang bent u in CM?: '))
        gewicht = int(input(' Hoe zwaar bent u in KG?:  '))
        certificaat = input(' heeft u een certififaat voor Overleven met gevaarlijk personeel? ja/nee ')

        if int(jsnor < 10) and (int(lengte < 150) and int(gewicht < 56)) and certificaat == 'nee':
            aangenomen = False
        
    elif gender == 'v':
        hoed = input(' Heeft u een hoge hoed? ja/nee: ')
        haar = input(' Heeft u roodkrulhaar? ja/nee: ')
        if haar == 'nee' and hoed == 'nee':
            aangenomen = False

        lengtehaar = int(input(' Hoelang is uw haar in CM?: '))
        lengte = int(input(' Hoelang bent u in CM?: '))
        gewicht = int(input(' Hoe zwaar bent u in KG?:  '))
        certificaat = input(' heeft u een certififaat voor Overleven met gevaarlijk personeel? ja/nee ')

        if int(lengtehaar < 20) and (int(lengte < 150) and int(gewicht < 56)) and certificaat == 'nee':
            aangenomen = False
            
    if aangenomen == True:
        print(' Heel goed gedaan, ' + name + ' , ' + 'u bent aangenomen!')
    elif aangenomen == False:
        print(' Helaas, u bent niet aangenomen') 
    
except ValueError as e:
    print(' Dat is geen nummer! vul alleen het getal in (bv: 130, 45 etc...')