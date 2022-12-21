getal = 50
nieuwgetal = getal+1
uitslag = nieuwgetal + getal
som = "50"

while uitslag < 1100:
    som = f"{som} + {nieuwgetal}"
    print(f"{som} = {uitslag}")
    nieuwgetal = nieuwgetal+1
    uitslag = uitslag + nieuwgetal

