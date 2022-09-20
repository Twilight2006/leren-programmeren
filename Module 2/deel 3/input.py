A = input(' vul een getal in: ') #2x hetzelfde getal doet raar: (<built-in function max> is het grootste getal)
B = input(' vul een getal in: ')

if A > B:
    max = A
elif B > A:
    max = B

print(str(max) + ' is het grootste getal ')

if A < B:
    min = A
elif B < A:
    min = B

print(str(min) + ' is het kleinste getal ')

if A == B:
    print(' A en B zijn gelijk ')
else:
    print(' A en B zijn niet gelijk ')










