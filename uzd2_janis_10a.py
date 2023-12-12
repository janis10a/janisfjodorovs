megin=3
tempinfo = {'1.decembris':3, #uztaisu vārdnīcu ar vērtībām un atslēgām
            '2.decembris':2,
            '3.decembris':4,
            '4.decembris':2,
            '5.decembris':2,
            '6.decembris':1,
            '7.decembris':5}
datums = input('ievadiet datumu(piemēram, 1.decembris)')#iegūstu datus no programmas izmantotāja
if datums in tempinfo: 
    print(datums,'temperetūra celsija grādos ir:',tempinfo[datums],'grādi.')
    print(datums,'temperetūra fāreneita grādos ir:',tempinfo[datums]*(9/5)+32,'grādi.')
else:
    print('Nepareiza atslēga. Lūdzu, ievadiet datumu no 1. līdz 7. decembrim.')
    while megin >0:#while cikls, lai zinātu, kad programmai jābeidzas
        megin = megin-1
        datums = input('ievadiet datumu(piemēram, 1.decembris)')
        if datums in tempinfo:
            print(datums,'temperetūra celsija grādos ir:',tempinfo[datums],'grādi.')
            exit() #beidz programmu, ja lietotājs iegūst atbildi par temperetūru.
        else:
            print('Nepareiza atslēga. Lūdzu, ievadiet datumu no 1. līdz 7. decembrim.')
            ()
        
