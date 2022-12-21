import random

ronde = 1
randomnum = 0
score = 0
geraden = 0

print("***************************************************************************")
print("")
print("Welkom bij: Raad Eens!")
print("In dit programma gaat u getal getal raden tussen de 1-1000!")
print("De regels zijn simpel:")
print("Je mag 10x raden per ronde")
print("Het maximale aantal rondes is 20, maar je kan eerder stoppen als je wilt!")
print("Aan het einde krijgt u een eindscore, veel succes!")
print("")
print("***************************************************************************")

while ronde <=20:
    y = 0
    randomnum = random.randint(1,1000)
    print(randomnum)
    print(f"Ronde: {ronde}")
    while y < 10:
        awnser = int(input("Voer een getal in tussen de 1 en de 1000: "))
        if awnser == randomnum:
            y = 10
            score+=1
            print("gefeliciteerd, u heeft het getal geraden!")
        elif awnser - randomnum <= 20 and awnser - randomnum > 0 or randomnum - awnser <= 20 and randomnum - awnser > 0:
            print("U bent heel warm")
        elif awnser - randomnum <= 50 and awnser - randomnum > 0 or randomnum - awnser <= 50 and randomnum - awnser > 0:
            print("U bent warm")
        elif awnser < randomnum:
            print("U moet hoger raden....")
        else:
            print("U moet lager raden.....")
        y+=1
        geraden +=1

    if ronde < 20:
        antwoord = input("Wilt u stoppen met spelen? Ja/Nee ").lower()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if antwoord == "ja":
            ronde = 20
    ronde += 1
