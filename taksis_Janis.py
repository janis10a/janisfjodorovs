cilveki = int(input('ievadiet cilvēku skaitu: '))
if cilveki <= 4:
    laiks = int(input('ievadiet pulksteņa laiku 24 stundu formātā:'))
    if laiks >=6 and laiks <= 22:
        print('jums par 1km jāmaksā €0,47')
        vieta = input('vai stacijā ir brīva stāvvieta? (ja/ne)')
        if vieta == 'ja':
                        gaidisana = int(input('ievadiet gaidīšanas laiku: '))
        if gaidisana >=0:
                print('par gaidīšanu jums būs jāmaksā €:',gaidisana*0.15 )
                cels = int(input('cik km jūs jāved? '))
                if cels >=0:
                    print('jums par ceļu būs jāmaksā€ ',0.47*cels)
        elif vieta == 'ne':
            print('par nolīgšanu būs jāmaksā €3,60')
            gaidisana = int(input('ievadiet gaidīšanas laiku: '))
            if gaidisana >=0:
                print('par gaidīšanu jums būs jāmaksā €:',gaidisana*0.15 )
                cels = int(input('cik km jūs jāved? '))
                if cels >=0:
                    print('jums par ceļu būs jāmaksā€ ',0.47*cels)
                    gaidisana = int(input('ievadiet gaidīšanas laiku: '))
            if gaidisana >=0:
                print('par gaidīšanu jums būs jāmaksā €:',gaidisana*0.15 )
                cels = int(input('cik km jūs jāved? '))
                if cels >=0:
                    print('jums par ceļu būs jāmaksā€ ',0.87*cels)
                    print('jūsu čeks: par ceļu jums jāmaksā',0.87*cels)
                    print('par noligsanu jums jamaksa 3.60' )
                    print('jums par gaidisanu jamaksa:',0.15*gaidisana)
        else:
            print('ievadiet pareizus datus.')
    elif laiks <=5 or laiks>=23:
        print('jums par 1km jāmaksā €0,87')
        vieta = input('vai stacijā ir brīva stāvvieta? (ja/ne)')
        if vieta == 'ja':
            print('nolīgšanas cena būs €1,20')
            gaidisana = int(input('ievadiet gaidīšanas laiku: '))
            if gaidisana >=0:
                print('par gaidīšanu jums būs jāmaksā €:',gaidisana*0.15 )
                cels = int(input('cik km jūs jāved? '))
                if cels >=0:
                    print('jums par ceļu būs jāmaksā€ ',0.87*cels)
                    print('jūsu čeks: par ceļu jums jāmaksā',0.87*cels)
                    print('par noligsanu jums jamaksa 1.20' )
                    print('jums par gaidisanu jamaksa:',0.15*gaidisana)
        elif vieta == 'ne':
            print('par nolīgšanu būs jāmaksā €3,60')
            gaidisana = int(input('ievadiet gaidīšanas laiku: '))
            if gaidisana >=0:
                print('par gaidīšanu jums būs jāmaksā €:',gaidisana*0.15 )
                cels = int(input('cik km jūs jāved? '))
                if cels >=0:
                    print('jums par ceļu būs jāmaksā€ ',0.87*cels)
                    print('jūsu čeks: par ceļu jums jāmaksā',0.87*cels)
                    print('par noligsanu jums jamaksa 3.60' )
                    print('jums par gaidisanu jamaksa:',0.15*gaidisana)
        else:
            print('ievadiet pareizus datus.')
            exit() 
else:
    print('mašīnā var būt tikai 4 pasažieri.')
    exit()


