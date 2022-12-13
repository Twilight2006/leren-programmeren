print("Important: This program is not finished yet, it is very rough around the edges.")
print("Since this is not the final version, please expect some bugs/inconsistenties.")
print("Also, the way the program calculates your score is inconsistent, so the result is likely wrong.")
print("Still, I hope you enjoy!")
print("Select language:")
taal = input("A:Nederlands B:English: ")

if taal == 'a':
    print("Loading......")
    naam = input("naam? : ")
    print("Hallo," , naam)
    print("Mooie naam heb je daar.....")
    print("Loading assests.....")
    print("Vragen voorbereiden.....")
    print("Bijna klaar.....")
    print("Hallo, ik welkom u tot:")
    print("------------------------------------------------")
    print("|                                              |")
    print("|     De ultieme Harry Potter House-quiz!      |")
    print("|Gryffindor, Slytherin, Ravenclaw of Hufflepuff|")
    print("|         Ontdek VANDAAG wat je bent!          |")
    print("|                                              |")
    print("------------------------------------------------")

    print("Deze quiz werkt als volgt:")
    print("Er zijn 5 gesloten vragen, die u moet beantwoorden.")
    print("Deze variëren van algemene Wizarding World-vragen tot situaties uit het echte leven.")
    print("Het programma zal beslissen in welk huis je bent op basis van de awnsers die je geeft.")
    print ("Opmerking: dit is misschien niet helemaal nauwkeurig, maar het programma doet hoe dan ook zijn best.")
    ready = False
    while ready == False:
        Ready = input("Klaar om te beginnen?: ")
        if Ready == 'Ja':
            ready = True
        elif Ready == 'ja':
            ready = True
        else:
            ready = False

    Gryffindor = "Jij bent Griffoendor! Je bent brutaal, gepassioneerd en moedig. Je hebt een sterk gedefinieerd gevoel van goed en kwaad, en je bent niet bang om je mening te uiten of te vechten voor wat je wilt."
    Slytherin = "Jij bent Zwadderich! Je bent sluw, vindingrijk en niet bang om de regels in je voordeel om te buigen. Je streeft er constant naar om vooruit te komen en zal er alles aan doen om in een machtspositie te komen."
    Ravenclaw = 'Jij bent Ravenklauw! Je bent wijs, opmerkzaam en stilletjes briljant. Je wordt misschien niet altijd meteen opgemerkt, maar je wordt alom gerespecteerd vanwege je humor en hersens.'
    Hufflepuff = "Jij bent Huffelpuf! Je bent gereserveerd, rationeel en nuchter. Je werkt goed samen met anderen, bent een geweldige teamspeler en je komt altijd op tegen onrecht."
    score = 0
    happy = False
    while happy == False:
        if ready == True:
            print("OK, dus.....")
            print("Vraag 1:")
            print("Wat is je favoriete kleur? A:rood B:groen C:blauw D:geel")
            q1 = input("Antwoord: ")
            if q1 == 'a':
                score = 2
            elif q1 == "b":
                score = 3
            elif q1 == "c":
                score = 4
            elif q1 == 'd':
                score = 1
            else:
                score = 0
            print("Berekenen.....")
            print("Volgende vraag;")
            print("vraag 2:")
            print("Wat is je favoriete dier?: A: Leeuw | B: Slang | C: Havik | D: Das")
            q2 = input('Antwoord: ')
            if q2 == 'a':
                score = score+2
            elif q2 == 'b':
                score = score+4
            elif q2 == 'c':
                score = score+1
            elif q2 == 'd':
                score = score+3

            print("Loading next question.....")
            print("Vraag 3:")
            print("Je betrapt je beste vriend op spieken tijdens een examen. wat doe je?: A: niets | B: vertel het aan de leraar | C: vertel ze dat het niet goed is | D: overtuig ze om het aan de leraar te vertellen.")
            q3 = input("Antwoord: ")
            if q3 == 'a':
                score = score+1
            elif q3 == 'b':
                score = score+4
            elif q3 == 'c':
                score = score+3
            elif q3 == 'd':
                score = score+2
            
            print("Je bent goed op weg", naam)
            print("OK, volgende vraag.....")
            print("Wat is je favoriete spreuk?: A:Stupefy | B:expelliarmus | C:Avada Kedavra | D:wingardium leviosa")
            q4 = input("Antwoord:")
            if q4 == 'a':
                score = score+2
            elif q4 == 'b':
                score = score+4
            elif q4 == 'c':
                score = score+1
            elif q4 == 'd':
                score = score+3
            
            print("Reviewing awnser.....")
            print("Volgende vraag!:")
            print("Wat zou je doen als je gevaar voelt?: A:Vertel de groep dat er iets niet klopt | B: ga alleen op pad | C: ineenkrimpen van angst | D: paniek zaaien in de groep")
            q5 = input("Antwoord: ")
            if q5 == 'a':
                score = score+3
            elif q5 == 'b':
                score = score+4
            elif q5 == 'c':
                score = score+1
            elif q5 == 'd':
                score = score+2
            
            print(score)

        if score > 14:
            print(Ravenclaw)  
            house = "Ravenclaw"
        elif score > 12:
            print(Gryffindor)
            house = "Gryffindor"
        elif score > 10:
            print(Slytherin)
            house = "Slytherin"
        elif score > 5:
            print(Hufflepuff)
            house = "Hufflepuff"

        tevreden = input("Ben je blij met dit resultaat?: ")
        if tevreden == 'ja':
            happy = True
            card = input("Wil je een kaartje?: ")
            if card == 'ja':
                print("---------------------------------")
                print(                                   )                             
                print( naam,                             )
                print( house, "huis"   ,                 )
                print(                                   )
                print("---------------------------------")
        elif tevreden == 'Ja':
            happy = True
            card = input("Wil je een kaartje?: ")
            if card == 'ja':
                print("---------------------------------")
                print(                                   )                             
                print( naam,                             )
                print( house, "huis"   ,                )
                print(                                   )
                print("---------------------------------")
            elif card == 'Ja':
                print("---------------------------------")
                print(                                   )                             
                print( naam,                             )
                print( house, "huis"   ,                )
                print(                                   )
                print("---------------------------------")
            else:
                print("Fijne dag nog!")


        else:
            happy = False

else:
    print("Loading......")
    naam = input("name? : ")
    print("Hello," , naam)
    print("Thats a nice name, you got there.....")
    print("Loading assests.....")
    print("Preparing questions.....")
    print("Almost done.....")
    print("Hello and welcome to:")
    print("------------------------------------------------")
    print("|                                              |")
    print("|     The Ultimate Harry potter House quiz!    |")
    print("|Gryffindor, Slytherin, Ravenclaw or Hufflepuff|")
    print("|         Find out what you are TODAY!         |")
    print("|                                              |")
    print("------------------------------------------------")

    print("This quiz works as follows:")
    print("There will be 5 closed questions, which you will have to anwser.")
    print("These range from general Wizarding World questions, to real life situations.")
    print("The program will decide what house you are in based on the awnsers you give.")
    print("Note: this might not be fully accurate, but the program tries its best regardless.")
    ready = False
    while ready == False:
        Ready = input("Are you ready to start?: ")
        if Ready == 'Yes':
            ready = True
        elif Ready == 'yes':
            ready = True
        else:
            ready = False

    Gryffindor = "You are Gryffindor! You are bold, passionate, and brave. You have a highly-defined sense of right and wrong, and you are not afraid to speak your mind or fight for what you want."
    Slytherin = "You are Slytherin! You are sneaky, resourceful, and not afraid to bend the rules to your advantage. You consistently strive to get ahead, and will do everything you can to be in a position of power."
    Ravenclaw = "You are Ravenclaw! You are wise, perceptive, and quietly brilliant. You may not always be noticed right away, but you are widely respected for your humor and brains."
    Hufflepuff = "You are Hufflepuff! You are reserved, rational, and down-to-earth. You work well with others, are a great team player, and you always take a stand against injustice."
    score = 0
    happy = False
    while happy == False:
        if ready == True:
            print("Alright, so.....")
            print("question 1:")
            print("What is your favourite color? A:red B:green C:blue D:yellow")
            q1 = input("Answer here: ")
            if q1 == 'a':
                score = 2
            elif q1 == "b":
                score = 3
            elif q1 == "c":
                score = 4
            elif q1 == 'd':
                score = 1
            else:
                score = 0
            print("Calculating.....")
            print("Next question;")
            print("question 2:")
            print("What is your favourite animal?: A:Lion | B:Snake | C:Hawk | D:Badger")
            q2 = input('Awnser here: ')
            if q2 == 'a':
                score = score+2
            elif q2 == 'b':
                score = score+4
            elif q2 == 'c':
                score = score+1
            elif q2 == 'd':
                score = score+3

            print("Loading next question.....")
            print("question 3:")
            print("You catch your best friend cheating on an exam. what do do you?: A:nothing | B:tell the teacher | C:tell them it is not right | D:convince them to tell the teacher.")
            q3 = input("Awnser here: ")
            if q3 == 'a':
                score = score+1
            elif q3 == 'b':
                score = score+4
            elif q3 == 'c':
                score = score+3
            elif q3 == 'd':
                score = score+2
            
            print("You are doing well", naam)
            print("Alright, next question.....")
            print("What is your favourite spell?: A:Stupefy | B:expelliarmus | C:Avada Kedavra | D:wingardium leviosa")
            q4 = input("Anwser here:")
            if q4 == 'a':
                score = score+2
            elif q4 == 'b':
                score = score+4
            elif q4 == 'c':
                score = score+1
            elif q4 == 'd':
                score = score+3
            
            print("Reviewing awnser.....")
            print("Next!:")
            print("What would you do if you sense danger?: A:Tell the group something isn't right | B:go out on your own | C:cower in fear |  D:spread panic in the group")
            q5 = input("Anwser here: ")
            if q5 == 'a':
                score = score+3
            elif q5 == 'b':
                score = score+4
            elif q5 == 'c':
                score = score+1
            elif q5 == 'd':
                score = score+2
            
            print(score)

        if score > 14:
            print(Ravenclaw)  
            house = "Ravenclaw"
        elif score > 12:
            print(Gryffindor)
            house = "Gryffindor"
        elif score > 10:
            print(Slytherin)
            house = "Slytherin"
        elif score > 5:
            print(Hufflepuff)
            house = "Hufflepuff"

        tevreden = input("Are you happy with this result?: ")
        if tevreden == 'yes':
            happy = True
            card = input("Do you want a card?: ")
            if card == 'yes':
                print("---------------------------------")
                print(                                   )                             
                print( naam,                             )
                print( house, "house"   ,                )
                print(                                   )
                print("---------------------------------")
        elif tevreden == 'Yes':
            happy = True
            card = input("Do you want a card?: ")
            if card == 'yes':
                print("---------------------------------")
                print(                                   )                             
                print( naam,                             )
                print( house, "house"   ,                )
                print(                                   )
                print("---------------------------------")
            elif card == 'Yes':
                print("---------------------------------")
                print(                                   )                             
                print( naam,                             )
                print( house, "house"   ,                )
                print(                                   )
                print("---------------------------------")
        else:
            print("Have a nice day!")


    else:
        happy = False



    
