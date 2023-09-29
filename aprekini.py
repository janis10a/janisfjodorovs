a = int(input('ievadi skaitli a:'))
b = int(input('ievadi skaitli b:'))
darb = input('+, -, *, /:')
if darb == '+':
    c = a+b
elif darb == '-':
    c = a-b
elif darb == '*':
    c = a*b
elif darb == '/':
    c = a/b
else:
    c = 'Kļūda'
print('Atbilde=', c)