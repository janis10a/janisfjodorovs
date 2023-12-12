prece=input('ievadiet preces nosaukumu: ')
cena=float(input('ievadiet preces cenu (1 vienība)'))
daudzums=int(input('ievadiet preces daudzumu: '))
saraksts=input('vai viss ir nopirkts, kas sarakstā?(j/n)')
if saraksts =='n':
    prece2=input('ievadiet preces nosaukumu: ')
    cena2=float(input('ievadiet preces cenu (1 vienība)'))
    daudzums2=int(input('ievadiet preces daudzumu: '))
    saraksts=input('vai viss ir nopirkts, kas sarakstā?(j/n)')
    if saraksts =='n':
        prece3=input('ievadiet preces nosaukumu: ')
        cena3=float(input('ievadiet preces cenu (1 vienība)'))
        daudzums3=int(input('ievadiet preces daudzumu: '))
        saraksts=input('vai viss ir nopirkts, kas sarakstā?(j/n)')
        if saraksts =='n':
            prece4=input('ievadiet preces nosaukumu: ')
            cena4=float(input('ievadiet preces cenu (1 vienība)'))
            daudzums4=int(input('ievadiet preces daudzumu: '))
            saraksts=input('vai viss ir nopirkts, kas sarakstā?(j/n)')
            if saraksts =='n':
                prece5=input('ievadiet preces nosaukumu: ')
                cena5=float(input('ievadiet preces cenu (1 vienība)'))
                daudzums5=int(input('ievadiet preces daudzumu: '))
                saraksts=input('vai viss ir nopirkts, kas sarakstā?(j/n)')
                if saraksts =='n':
                    prece6=input('ievadiet preces nosaukumu: ')
                    cena6=float(input('ievadiet preces cenu (1 vienība)'))
                    daudzums6=int(input('ievadiet preces daudzumu: '))
                    saraksts=input('vai viss ir nopirkts, kas sarakstā?(j/n)')
elif saraksts=='j':
        veikals = input('kurā veikalā jūs iepirkāties?(top, sena bode, elvi, rimi, raibais suns)')
        if veikals=='top':
             print('jums šajā veikalā būs 30 procentu atlaide')
             ceks=input('vai jums vajag čeku? (j/n)')
             if ceks=='j':
                 print('jūsu pirkums ir: ',daudzums,prece,'jums izmaksās',daudzums*cena*70/100,'eiro')
        elif veikals=='sena bode':
            print('jums šajā veikalā būs 40 procentu atlaide, ja ir karte.')
            ceks=input('vai jums vajag čeku? (j/n)')
            if ceks=='j':
                print('jūsu pirkums ir: ',daudzums,prece,'jums izmaksās',daudzums*cena*60/100,'eiro')
        elif veikals=='rimi':
            print('jums šajā veikalā būs 20 procentu atlaide, bet 50 procentu atlaide, ja ir karte.')
            ceks=input('vai jums vajag čeku? (j/n)')
            if ceks=='j':
                print('jūsu pirkums ir: ',daudzums,prece,'jums izmaksās',daudzums*cena*80/100,'eiro')
        elif veikals=='elvi':
            print('jums būs 30 procentu atlaide, ja pērc 3 vai vairāk preces.')
            ceks=input('vai jums vajag čeku? (j/n)')
            if ceks=='j':
                print('jūsu pirkums ir: ',daudzums,prece,'jums izmaksās',daudzums*cena,'eiro')
        elif veikals=='raibais suns':
            print('jums katra otrā prece ir par brīvu.')
            ceks=input('vai jums vajag čeku? (j/n)')
            if ceks=='j':
                print('jūsu pirkums ir: ',daudzums,prece,'jums izmaksās',daudzums*cena,'eiro')
    
