gadi = int(input('ievadiet suņa gadus'))
if gadi <= 2:
    print('jūsu sunim suņa gados ir ',gadi*10.5,' gadi!')
elif gadi >2:
    print('jūsu sunim suņa gados ir ',21+(gadi-2)*4,' gadi!')
elif gadi <0:
    print('ievadiet pareizus datus.')