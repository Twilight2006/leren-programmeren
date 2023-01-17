verder = True
lijstje = {

}

while verder == True:
        item = input("Wat wilt u toevoegen?: ").lower()
        aantal = input("En hoeveel ervan?: ")

        if item in lijstje.keys():
                lijstje[item]+=int(aantal)
        else:
                lijstje[item]=int(aantal)

        print(lijstje)

        meer = input("Wilt u meer toevoegen?: ")
        if meer == 'ja':
                verder = True
        else:
                verder = False
                print("<-<- Uw boodschappenlijstje ->->")
                for item in lijstje:
                        print(lijstje[item], "x", item)



