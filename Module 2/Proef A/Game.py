print('Welkom bij return of the kongs!')
print('----------------- betekent dat het verhaal daaronder verdergaat.')
print('In vorige versies vas het moeilijk om te zien waar je verder moet lezen')
name = input('Vul uw naam in AUB: ')

print('Het is een stille nacht voor ' + name)
print('Todat ' + name + ' een raar geluid hoort in de slaapkamer')
Choice1 = input('Wat gaat ' + name + ' doen? A: niks. B:ga kijken ')

if Choice1 == 'a':
    print('-----------------')
    print(name + ' blijft liggen in bed.')
    print('Er gebeurt niks en ' + name + ' blijft liggen')
    print('----The end----')
elif Choice1 == 'b':
    print('-----------------')
    print(name + ' gaat kijken in de hoek')
    print('als ' + name + ' dichterbij komt, wordt ' + name + 'duizelig')
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
             print('Na een korte 5 minuten lopen, komen' + name + ' bij de tempel aan.')



         elif Help == 'b':
             print('-----------------')
             print('Nee, Donkey. Liever niet, zei ' + name)
             print('Donkey zijn gezicht gaat van blij naar... boos?')
             print('Dan springt Donkey op ' + name + 'af.')
             print('Dan voelt' + name + ' gedoemd om nooit meer wakker te worden...')
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