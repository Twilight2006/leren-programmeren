print(' hallo meneer/mevrouw, ' )
print(' we gaan u een paar vragen stellen om te zien ')
print(' ofdat u de verseiste ervaring heeft. ' )
print(' op basis van uw antwoorden laten we u weten ' )
print(' ofdat u bent aangenomen of afgewezen. ' )

man = input('bent u een man? : ')
if man == 'ja':
    diploma = input(' heeft u een mbo-4 diploma ondernemen? ja/nee : ' )
    rijbewijs = input(' heeft u een geldig vrachtwagen rijbewijs? ja/nee : ')
    hoed = input(' heeft u een hoge hoed? ja/nee :')
    snor = input(' heeft u een snor? ja/nee : ')
    if snor == 'ja':
        snorl = input(' is uw snor 10 cm of breder? ja/nee : ')
        lengte = input(' wat is uw lengte in cm? ')
        gewicht = input(' hoeveel weegt kg weegt u? : ')
        certificaat = input(' heeft u een certififaat voor Overleven met gevaarlijk personeel? ja/nee ')
        dd = input(' hoeveel jaar ervaring heeft u met dieren-dressuur? :')
        acrobatiek = input(' hoeveel jaar ervaring heeft u met acrobatiek? : ')
        jongleren = input(' hoeveel jaar ervaring heeft u met jongleren? :')


    elif snor == 'nee':
        lengte = input(' wat is uw lengte in cm? ')
        gewicht = input(' hoeveel weegt kg weegt u? : ')
        certificaat = input(' heeft u een certififaat voor Overleven met gevaarlijk personeel? ja/nee ')
        dd = input(' hoeveel jaar ervaring heeft u met dieren-dressuur? :')
        acrobatiek = input(' hoeveel jaar ervaring heeft u met acrobatiek? : ')
        jongleren = input(' hoeveel jaar ervaring heeft u met jongleren? :')

elif man == 'nee':
    diploma = input(' heeft u een mbo-4 diploma ondernemen? ja/nee : ' )
    rijbewijs = input(' heeft u een geldig vrachtwagen rijbewijs? ja/nee : ')
    hoed = input(' heeft u een hoge hoed? ja/nee :')
    haar = input(' heeft u rood haar? ja/nee : ')
    if haar == 'ja':
        haar1 = input(' hoelang is uw haar in centimeter? ja/nee : ')
        lengte = input(' wat is uw lengte? ')
        gewicht = input(' hoeveel weegt kg weegt u? : ')
        certificaat = input(' heeft u een certififaat voor Overleven met gevaarlijk personeel? ja/nee ')
        dd = input(' hoeveel jaar ervaring heeft u met dieren-dressuur? :')
        acrobatiek = input(' hoeveel jaar ervaring heeft u met acrobatiek? : ')
        jongleren = input(' hoeveel jaar ervaring heeft u met jongleren? :')
    
    elif haar == 'nee':
        lengte = input(' wat is uw lengte? ')
        gewicht = input(' hoeveel weegt kg weegt u? : ')
        certificaat = input(' heeft u een certififaat voor Overleven met gevaarlijk personeel? ja/nee ')
        dd = input(' hoeveel jaar ervaring heeft u met dieren-dressuur? :')
        acrobatiek = input(' hoeveel jaar ervaring heeft u met acrobatiek? : ')
        jongleren = input(' hoeveel jaar ervaring heeft u met jongleren? :')

else:
    print(' dat is geen mogelijkheid ')

hasdipolma = True 












    




