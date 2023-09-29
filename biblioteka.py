nenodots = input('vai pie jums atrodas kāds laikā nenodots izdevums? ') 
if nenodots == 'jā':
    print('atvainojos, bet jums grāmatu nevaram izsniegt.')
if nenodots == 'nē':
    print('nākamā pārbaude.')

pieprasīta = input('vai publikācija ko vēlies ir pieprasīta? ')
if pieprasīta == 'jā':
    print('mēs jums varam aizdot uz 2 dienām.')
else: 
    print('nākamā pārbaude.')

publikacija = input('vai jūs vēlaties publikāciju vai žurnālu? ' )
if publikacija == "publikāciju":
    print('mēs jums šo publikāciju varam izsniegt uz 7 dienām.')
else:
    print('nākamā pārbaude.')

NoPersonala = input('vai tā ir no personāla? ')
if NoPersonala == 'jā':
    print('žurnālu jums aizdosim uz 28 dienām')
else:
    print('žurnālu jums aizdosim uz 14 dienām.')