getal = 50
nieuwgetal = getal+1
uitslag = nieuwgetal + getal
strsom = "50 + 51"
print("50 + 51 = 101")

while uitslag < 1100:
    nieuwgetal = nieuwgetal+1
    uitslag = uitslag + nieuwgetal
    strsom = str(strsom) + '+' + str(nieuwgetal) + "=" + str(uitslag)
    print(strsom)
