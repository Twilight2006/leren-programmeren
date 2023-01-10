dagenlist = ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag"]

workdays = dagenlist[0:5]
weekend = dagenlist[5:7]
daysR = tuple(reversed(dagenlist))
workdaysR = tuple(reversed(workdays))
weekendR = tuple(reversed(weekend))

print("Alle dagen van de week zijn: ", dagenlist)
print("Alle weekdagen van de week zijn: ", workdays)
print("Alle weekenddagen van de week zijn: ",weekend)
print("Alle dagen van de week in omgekeerde volgorde zijn: ",daysR)
print("De werkdagen in omgekeerde volgorde zijn: ",workdaysR)
print("De weekenddagen in omgekeerde volgorde zijn: ",weekendR)
print("Done")