
prijssmall = 3.99
prijsmedium = 6.99
prijslarge = 10.99

try:
    print('hallo, welkom bij de online pizzaria!')
    print('kijk naar de lijst. welke pizza wilt u?')
    print('small : 3,99 per/stuk')
    print('medium : 6,99 per/stuk')
    print('large : 10,99 per/stuk')
    totaalsmall = int(input('hoeveel small wilt u? '))
    totaalmedium = int(input('hoeveel medium wilt u? '))
    totaallarge = int(input('hoeveel large wilt u? '))
    print('dat wordt dan ' +  str(prijssmall * totaalsmall + prijsmedium * totaalmedium + prijslarge * totaallarge) + ' euro alstulieft ')
    print('------------------------------------')
    print(' aantal small: ' + str(totaalsmall))
    print(' aantal medium: ' + str(totaalmedium))
    print(' aantal large: ' + str(totaallarge))
    print('------------------------------------')
    

except ZeroDivisionError as e:
    print('dat is niet mogelijk')

except ValueError as e:
    print('dat is geen nummer!')

except TypeError as e:  
    print('u heeft het verkeerd ingevuld! ') 

finally:
    print('kom nog eens langs!')
