keuze = (input("Wat wilt u doen? 1:optellen 2:aftrekken 3:vermeningvuldigen 4:delen : "))
getal1 = int(input("Voer getal in: "))
getal2 = int(input("Voer getal in: "))

if keuze == '1':
    antwoord = getal1 + getal2
    print(antwoord)
elif keuze == '2':
    antwoord = getal1 - getal2
    print(antwoord)
elif keuze == '3':
    antwoord = getal1*getal2
    print(antwoord)
elif keuze == '4':
    antwoord = getal1/getal2
    print(antwoord)
else:
    print("Dat is geen mogelijkheid.")