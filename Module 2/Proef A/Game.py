print('Welkom bij return of the kongs!')
print('----------------- betekent dat het verhaal daaronder verdergaat.')
print('In vorige versies vas het moeilijk om te zien waar je verder moet lezen')
name = input('Vul uw naam in AUB: ')

print('Het is een stille nacht voor ' + name)
print('Todat ' + name + ' een raar geluid hoort in de slaapkamer')
Choice1 = input('Wat gaat ' + name + ' doen? A: niks. B:ga kijken ').lower()

if Choice1 == 'a':
    print('-----------------')
    print(name + ' blijft liggen in bed.')
    print('Er gebeurt niks en ' + name + ' blijft liggen')
    print('----The end----')
elif Choice1 == 'b':
    print('-----------------')
    print(name + ' gaat kijken in de hoek')
    print('als ' + name + ' dichterbij komt, wordt ' + name + ' duizelig')
    print(name + ' valt in een diepe slaap')
    print('----3 dagen later----')
    print(name + ' wordt wakker')
    print(name + ' kijkt rond de kamer')
    print('Dan opent een deur')
    Hide = input('Wat doet ' + name + '? A:Blijf zitten in het bed. B:Verstop je onder de dekens. ')
    if Hide == 'a':
         print('-----------------')
         print('Er komt een vaag figuur naar binnen...')
         print('Is dat... DONKEY KONG?')
         print('Ja hoor, er komt een Donkey Kong uit de deur.')
         print('Hij loopt naar ' + name + ' toe')
         print('Je bent sterk, we hebben je nodig' ',' 'Dat waren de woorden die uit Donkey komen')
         print(name + ' besluit om naar Donkey te luisteren')
         print('Onze schat is gestolen, we hebben jouw hulp nodig')
         Help = input('Wil je ons helpen de schat terug te krijgen?' 'Wat zegt ' + name + '?' + 'A:ja. B:nee')
         if Help == 'a':
             print('-----------------')
             print('Ja hoor, dat wil ik wel, zei ' + name)
             print('Dan begint Donkey te dansen.')
             print('Volgensmij is hij blij.')
             print('Dan zegt Donkey het volgende:')
             print('Volg mij mee naar buiten, ik leid je naar een tempel.')
             print(name + ' is niet zeker, maar volgt Donkey naar buiten.')
             print('Na een korte 5 minuten lopen, komen Donkey en ' + name + ' bij de tempel aan.')
             print('Als ' + name + ' bij de ingang staat, rent Donkey Kong weg, zonder iets te zeggen.')
             print('Dan gaat ' + name + ' naar binnen')
             print('Na wat voelt als een eeuwigheid van trappenlopen, komt ' + name + ' in een grote hal')
             print('De hal heeft twee gangen, een links en een rechts pad')
             pad = input('Welk pad kiest ' + name +'?' 'A:links. B:rechts. ')
             if pad == 'a':
                 print('-----------------')
                 print(name + ' gaat naar links')
                 print(name + ' komt in een kleine ruimte, met een gigantische speaker op het plafond')
                 print('Dan begint de speaker geluid te maken.')
                 awnser = input('Oh THZOU WHO ENTERED TZHIS CURSED LAND, WHAT IZT 5+5x2:3+1? Round UP^ : ')
                 if awnser == '8':
                    print('-----------------')
                    print('De speaker gaat weg.')
                    print(name + ' heeft het juist beantwoord, nu kan ' + name + ' verder!')
                    print(name + ' gaat door de deur die open is gegaan')
                    print('Na een paar minuten lopen door een smalle gang, komt ' + name + ' in een grote hal')
                    print('Daar staat een kist, midden in de kamer.')
                    print(name + ' opent de kist, wat is de schat?')
                    print('is dat..... een BANAAN?')
                    print('Donkey kong zijn schat was een banaan?')
                    print('----END----')
                 else:
                    print('Dan komen de muren naar ' + name + 'toe...')
                    print('----The End----')

             elif pad == 'b':
                print('-----------------')
                print(name + ' gaat naar rechts')
                print(name + ' komt in een grote ruimte, met maar 1 voorwerp.')
                print('Een bord')
                print('Het bord leest alstvolgt:')
                print('Oh, Tzou who Enzter This place, Tell me, Are Tzou Honest?')
                print('I have a Question for Tzou, Are Tzou supposed to be in zhis world?')
                honest = input('Are you from this world or no, dont try to pleaze me. A: ja. B:Nee. ')
                if honest == 'a':
                    print('-----------------')
                    print('ja, ik ben van deze wereld, zei ' + name)
                    print('De grond gaat open, en ' + name + ' valt in een gigantische afgrond')
                    print('Niemand weet wat er daarna is gebeurt...')
                    print('----The End----')

                elif honest == 'b':
                    print('-----------------')
                    print('nee, ik ben niet van deze wereld, zei ' + name)
                    print('Het bord zakt de grond in, en een deur gaat open')
                    print(name + ' kan nu verder!')
                    print(name + ' gaat door de deur die open is gegaan')
                    print(name + 'gaat door de deur die open is gegaan')
                    print('Na een paar minuten lopen door een smalle gang, komt ' + name + ' in een grote hal')
                    print('Daar staat een kist, midden in de kamer.')
                    print(name + ' opent de kist, wat is de schat?')
                    print('is dat..... een BANAAN?')
                    print('Donkey kong zijn schat was een banaan?')
                    print('----END----')
                    

                else:
                    print('Dat is geen mogelijkheid!')

         elif Help == 'b':
             print('-----------------')
             print('Nee, Donkey. Liever niet, zei ' + name)
             print('Donkey zijn gezicht gaat van blij naar... boos?')
             print('Dan springt Donkey op ' + name + ' af.')
             print('Dan voelt ' + name + ' niks meer... gedoemd om nooit meer wakker te worden...')
             print('---- The End----')
        
         else:
            print('Dat is geen mogelijkheid!')

    elif Hide == 'b':
         print('-----------------')
         print(name + ' verstopt zich onder de dekens.')
         print('Dan hoort ' + name + ' stappen binnen komen')
         print('De dekens worden omhoog getrokken, daarna voelt ' + name + ' een steek in de buik')
         print('De laatste woorden die ' + name + ' hoort, zijn als volgt:')
         print('We hebben niks aan watjes, slaap nu')
         print('---- The End----')

    else:
        print('Dat is geen mogelijkheid!')


else:
    print('Dat is geen mogelijkheid!')