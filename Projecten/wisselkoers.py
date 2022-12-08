euro = 1.00
dollar = 1.05
pond = 0.86
af = False

while af == False:
    print("Welkom bij de wisselbank, Wat wil je berekenen?")
    Waarde1 = input("Wat is uw eerste Valuta? (Euro,Dollar,Pond) : ")
    Waarde2 = input("Wat is uw tweede Valuta? (Euro,Dollar,Pond) : ")
    print("Het volgende wordt berekent: ", Waarde1, "->", Waarde2)

    if Waarde1 == "Euro":
        Waarde1 = euro
        waardeX = input("Hoeveel euro? : ")
    elif Waarde1 == "Dollar":
        Waarde1 = dollar
        waardeX = input("Hoeveel dollar? :")
    elif Waarde1 == "Pond":
        Waarde1 = pond
        waardeX = input("Hoeveel pond? : ")
    else:
        print("Error: Uw eerste Valuta is geen bekende waarde")

    if Waarde2 == "Euro":
        Waarde2 = euro
    elif Waarde2 == "Dollar":
        Waarde2 = dollar
    elif Waarde2 == "Pond":
        Waarde2 = pond
    else:
        print("Error: Uw tweede Valuta is geen bekende waarde")

    Val1 = waardeX

    totaal = int(waardeX) * Waarde2

    print("De nieuwe waarde is", totaal)
    if totaal > 0:
        afgerond = input("Bent u klaar? Ja/Nee : ")
        if afgerond == "Ja":
            print("Kom nog een keer terug!")
            af = True
    else:
        af = False

