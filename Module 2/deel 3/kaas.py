print(' hallo meneer/mevrouw, ik ben kaasbot en ik ga proberen te raden welke kaas u in uw hoofd hebt! ')
print(' ik ga u een paar vragen stellen waarop u antwoord moet geven, bliep bloep!')

geel = input(' is de kaas geel of niet? ja/nee : ')

if geel == 'nee':
    schimmel = input(' heeft de kaas blauwe schimmel? : ')
    if schimmel == 'ja':
        korst = input(' heeft de kaas korst? : ')
    if korst == 'nee':
        print(' is uw kaas fourme d' 'ambert? ' )
    elif korst == 'ja':
            print('is uw kaas Blue de Rochbaron?')

    elif schimmel == 'nee':
        korst2 = input(' heeft de kaas korst? : ')
    if korst2 == 'ja':
        print('is uw kaas Camembert?')
    elif korst2 == 'nee':
            print('is uw kaas Mozzarella?')

                 


elif geel == 'ja':
    gaten = input(' heeft de kaas gaten? : ')
    if gaten == 'ja':
        prijs = input(' is de kaas belagelijk duur? : ') 
        if prijs == 'nee':
            print('is uw kaas Leerdammer? ')
        elif prijs == 'ja':
                print('is uw kaas Emmenthaler? ')
        
    elif gaten == 'nee':
            hard = input(' is de kaas belagelijk hard? : ')
            if hard == 'ja':
                print(' is uw kaas Parmigiano Reggiano? ')
            elif hard == 'nee':
                print(' is uw kaas Goudsekaas? ')

else:
    print(' error-error-error,kzzr dat is geen kzzzzrztt mogelijkheid kzzrzzt')
            
        
      

