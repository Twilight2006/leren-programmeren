print('Welkom bij: Return of the Kongs!')
print('Deze game gaat meer om het verhaal')
name = input('Vul uw naam in AUB: ')

print('Het is een stille nacht......')
print('Meestal kijk je in bed nog tot ongeveer 1 uur op je telefoon tot je echt gaat slapen.')
print('Maar vandaag was anders.')
print('Je hebt het gevoel dat er iets naar je kijkt.')
print('In het donker....')
print('Wat ge je doen?')
antwoord = input('A: Blijf liggen / B: Ga kijken ' ': ')
if antwoord == 'a':
    print('Je blijft in je bed liggen, en gaat gewoon door zoals normaal.')
    print('---Einde---')
elif antwoord =='b':
    print('Je gaat naar de hoek van je kamer, waar je denkt dat er iets naar je aan het kijken is.')
    print('Als je dichterbij komt, voel je een steek in je zij. Je begint stemmen in je hoofd te horen.')
    print('?: ooh ooh ah?')
    print('Wat is dit?')
    print('Je voelt jezelf wegdrijven in een diepe slaap...')
    print('Je wordt wakker na wat voelt als een eeuwigheid.')
    print('Je voelt je een beetje duizelig, maar het is nog wel te doen.')
    print('Je doet je ogen open en strekt.')
    print('Je bent niet in je eigen kamer!')
    print('Waar ben ik?')
    print('Je slaat jezelf.')
    print('Toen jejezelf raakte, voelde je een raar soort haar...')
    print('Je kijkt naar je hand.')
    print('Je kan je ogen niet geloven. Nee, je WILT je ogen niet geloven.')
    print('BEN JE EEN AAP GEWORDEN? ')
    print('Riep ' + name + ' zo hard als die kon.')
    print('Daarna opent er een deur....')
    print('Wacht....')
    print('Is dat.....')
    print('DONKEY KONG?')
    print('Ja hoor, er komt een Donkey Kong uit de deur.')
    print('ooh ooh ha hahaa ooh? ' + '(Hallo, ' + name  + '!)')
    print('Waarom kan je hem verstaan?')
    print('ooooohhooooooohoooohoooooi!' '(Ik heb je meegenomen naar onze wereld omdat je ons moet helpen!)')
    print('ooh ooh ah ah' + '(Onze schat is gestolen, wil je ons alsjeblieft helpen ' + ', ' +  name + '?)')
    help = input('Wat zeg je?: A:nee / B:ja  ')
    if help == 'a':
        print('Waarom springt Donkey Kong op je af? Waarom... Ziet ie er boos uit? ')
        print('---Einde---')
    elif help == 'b':
        print('oooh hooo hooi' '(Dankje, ' +  name + '.' + 'Zie je die tempel daar? Daar is onze schat. Iemand heeft onze schat daarheen gebracht.)')
        print('OK, leid me maar de weg, Donkey Kong!')
        print('hooohooohaha' + '(Wacht, ' +  name + ' klinkt niet als een aap, er moet een mooie naam achter! Wat vind je van ' + name + ' kong?)')
        kong = input('Wat zeg je? A:nee / B:ja : ')
        if kong == 'a':
            print('Nee, dat wil ik niet. Dat vindt ik geen leuke naam.')
            print('Dat vindt Donkey Kong niet leuk.')
            print('ooooh ooh ooha ' + ' (Je maakt traditie kapot. Weg met jou!)')
            print('---GAME OVER---')
        elif kong == 'b':
            print('Ja hoor, noem me maar ' + name + ' kong ')
            print('Terwijl jullie 2 naar de tempel lopen, begin je een beetje te twijfelen.')
            print('Maar je gaat nu niets meer terug. Je gaat ervoor.')
            print('Je komt de tempel in.')
            print('Donkey Kong zwaait je na en loopt terug naar het huis waar jullie vandaan komen.')
            print('Je loopt de trappen af.')
            print('Sheesh, dit zijn wel heel veel trappen.')
            print('Je blijft doorlopen, totdat je onderaan komt.')
            print('Na een paar minuten, kom je beneden.')
            print('Je ziet een grote hal, met twee kanten.')
            print('Oh nee.')
            print('Je moet kiezen tussen twee kanten. welke kant kies je?')
            side = input('Kies wijs: links of Rechts?: A-links / B-rechts : ')
            if side == 'a':
                print('Je gaat de linkse kamer in')
                print('Hij is nogal donker, maar je kan nog wel dingen zien.')
                print('Ooooooh boy')
                print('Nu begint het.')
                print('Je ziet een gigantische dobbelsteen, met een bord daarnaast.')
                print('{Oh, thzou who will be poor enough to enter zhis cursed tzemple,')
                print('Thzou will not pass without a zbrain.')
                print('Thzou will have to choose a anwser based on what i ask Tzhou,')
                print('Good ZLuck poor Zhoul.}')
                print('Opeens hoor je uit een gigantische luidspreker in je oor roepen..')
                awnser = input('Oh THZOU WHO ENTERED TZHIS CURSED LAND, WHAT IZT 5+5x2:3+1? Round UP^ : ')
                if awnser == '8':
                    print('De speaker gaat weg.')
                    print('Je hebt het juist beantwoord, nu kan je verder!')

                else:
                    print('Als het voor een paar secoden stilblijft, begin je te stressen.')
                    print('Dan komen de muren op je af....')
                    print('---GAME OVER---')

               


            elif side == 'b':
                print('Je gaat de rechtse kamer in')
                print('Het eerste wat je ziet makkt je nu al bang:')
                print('een Gigantisch standbeeld van een spin....')
                print('Je kijkt naar achter om te kijken of je nog terug kan.')
                print('De deur is dicht.')
                print('Het spinnenbeeld begint te Praten..')
                print('Oh you who enter this land, you have lots and lots of courage..')
                print('you have a VERY courages heart. So tell me, are you REALLY a monkey,')
                print('or have your friends transformed you?')
                print('Je staat stil van angst.')
                print('AWNSER ME! OR I UNLEASH MY FURY!')
                print('o-ohh---k . Ok.')
                print('Ik ben')
                spin = input('Wat zeg je? :')
                
                
            else:
                print('Dat is geen mogelijkheid, Restarting program...(herstart het programma)')

    else:
        print('Dat is geen mogelijkheid, Restarting program...(herstart het programma)')
    
    
else:
    print('Dat is geen mogelijkheid, Restarting program...(herstart het programma)')