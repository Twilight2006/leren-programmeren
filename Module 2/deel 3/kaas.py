print(' hallo meneer/mevrouw, ik ben kaasbot en ik ga proberen te raden welke kaas u in uw hoofd hebt! ')
print(' ik ga u een paar vragen stellen waarop u antwoord moet geven ')

geel = input(' is de kaas geel of niet? J/N : ')

if geel == 'nee':
    schimmel = input(' heeft de kaas blauwe schimmel? : ')
    if schimmel == 'ja':
        korst = input(' heeft de kaas korst? : ')
    if korst == 'nee':
        aw1 = input(' is uw kaas fourme d' 'ambert? : ' )
        if aw1 == 'ja':
                print(' dankuwel voor het spelen ^_^ ')
        elif aw1 == 'nee':
                    print('oeps, sorry. herstart mijn programma om het opnieuw te proberen, krzzzt! ')

    
    elif korst == 'ja':
            aw2 = input('is uw kaas Blue de Rochbaron? :')
            if aw2 == 'ja':
                print(' dankuwel voor het spelen ^_^ ')
            elif aw2 == 'nee':
                    print('oeps, sorry. herstart mijn programma om het opnieuw te proberen, krzzzt! ')

    elif schimmel == 'nee':
        korst2 = input(' heeft de kaas korst? : ')
    if korst2 == 'ja':
        aw3 = input('is uw kaas Camembert? :')

    if aw3 == 'ja':
                print(' dankuwel voor het spelen ^_^ ')
    elif aw3 == 'nee':
                print('oeps, sorry. herstart mijn programma om het opnieuw te proberen, krzzzt! ')
        


    elif korst2 == 'nee':
            aw4 = input('is uw kaas Mozzarella? :')
            if aw4 == 'ja':
                print(' dankuwel voor het spelen ^_^ ')
            elif aw4 == 'nee':
                    print('oeps, sorry. herstart mijn programma om het opnieuw te proberen, krzzzt! ')

                 


elif geel == 'ja':
    gaten = input(' heeft de kaas gaten? : ')
    if gaten == 'ja':
        prijs = input(' is de kaas belagelijk duur? : ') 
        if prijs == 'nee':
            aw5 = input('is uw kaas Leerdammer? : ')
            if aw5 == 'ja':
                print(' dankuwel voor het spelen ^_^ ')
            elif aw5 == 'nee':
                    print('oeps, sorry. herstart mijn programma om het opnieuw te proberen, krzzzt! ')
            

        elif prijs == 'ja':
                aw6 = input('is uw kaas Emmenthaler? :')
                if aw6 == 'ja':
                    print(' dankuwel voor het spelen ^_^ ')
                elif aw6 == 'nee':
                    print('oeps, sorry. herstart mijn programma om het opnieuw te proberen, krzzzt! ')
        
    elif gaten == 'nee':
            hard = input(' is de kaas belagelijk hard? : ')
            if hard == 'ja':
                aw7 = input(' is uw kaas Parmigiano Reggiano? : ')
            if aw7 == 'ja':
                print(' dankuwel voor het spelen ^_^ ')
            elif aw7 == 'nee':
                    print('oeps, sorry. herstart mijn programma om het opnieuw te proberen, krzzzt! ')

            elif hard == 'nee':
                aw8 = input(' is uw kaas Goudsekaas? : ')
                if aw8 == 'ja':
                    print(' dankuwel voor het spelen ^_^ ')
                elif aw8 == 'nee':
                    print('oeps, sorry. herstart mijn programma om het opnieuw te proberen, krzzzt! ')


    else:
        print(' error-error-error,kzzr dat is geen mogelijkheid kzzzzt')
            
        
      

