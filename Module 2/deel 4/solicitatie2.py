try:
    print('Hallo, welkom bij de solicitatie! ')
    print('We gaan u een paar vragen stellen.')
    print('Op basis van uw antwoorden laten we u weten of u bent aangenomen of niet.')
    name = input('Wat is uw naam? ')
    if name == 'sven':
        raise NameError('U mag niet dezelfde naam hebben als de eigenaar! ')
    print('Hallo ' + name )
    gender = input('Bent u een man of een vrouw? ')
    if gender == 'man' or 'Man' :
            diploma = input('Heeft u een MBO-4 diploma? ja/nee : ')
            rijbewijs = input('heeft u een geldig vrachtwagen rijbewijs? ja/nee : ')
            hoed = input('heeft u een hoge hoed? ja/nee :')
            snor = input('heeft u een snor? ja/nee : ')
            if snor == 'ja' or 'Ja':
                jsnor = input('Is uw snor langer dan 10 cm? ja/nee : ')
                lengte = input('Bent u langer dan 150 cm? ')
                gewicht = input('Bent u zwaarder dan 80 kg? : ')
                certificaat = input('Heeft u een certififaat voor Overleven met gevaarlijk personeel? ja/nee ')
                dd = int(input('Hoeveel jaar ervaring heeft u met dieren-dressuur? :'))
                acrobatiek = int(input('Hoeveel jaar ervaring heeft u met acrobatiek? : '))
                jongleren = int(input('Hoeveel jaar ervaring heeft u met jongleren? :'))
            elif snor =='nee' or 'Nee':
                print('Sorry meneer, u moet een snor hebben.')
    

    elif gender == 'vrouw' or 'Vrouw' :
            diploma = input('Heeft u een MBO-4 diploma?: ')
            rijbewijs = input('Heeft u een geldig vrachtwagen rijbewijs? ja/nee : ')
            hoed = input('Heeft u een hoge hoed? ja/nee :')
            haar = input('Heeft u lang rood haar? ja/nee :')
            if haar == 'ja' or 'Ja':
                haar1 = input('Is uw haar langer dan 20 cm? ja/nee : ')
                lengte = input('bent u langer dan 150 cm? ')
                gewicht = input('bent u zwaarder dan 80 kg? : ')
                certificaat = input('heeft u een certififaat voor Overleven met gevaarlijk personeel? ja/nee ')
                dd = int(input('Hoeveel jaar ervaring heeft u met dieren-dressuur? :'))
                acrobatiek = int(input('hoeveel jaar ervaring heeft u met acrobatiek? : '))
                jongleren = int(input('hoeveel jaar ervaring heeft u met jongleren? :' ))
            elif haar == 'nee' or 'Nee':
                print('Sorry mevrouw, u moet lang rood haar hebben')

                            
                            
except NameError as e:
    print('U mag niet dezelfde naam hebben als de eigenaar!')

except ValueError as e:
    print('Vul de volgende keer een nummer in bruh')

finally:
    print('Dankuwel voor uw solicitatie! ')

if gender == 'man':
    if diploma == 'ja':
            if rijbewijs == 'ja':
                    if hoed == 'ja':
                        if snor == 'ja':
                            if jsnor == 'ja':
                                if lengte == 'ja':
                                    if gewicht == 'ja':
                                        if certificaat == 'ja':
                                             print(' u bent aangenomen! ')

elif gender == 'vrouw':
    if diploma == 'ja':
        if rijbewijs == 'ja':
                if hoed == 'ja':
                    if snor == 'ja':
                        if jsnor == 'ja':
                            if lengte == 'ja':
                                if gewicht == 'ja':
                                    if certificaat == 'ja':
                                            print(' u bent aangenomen! ')

















            

