stop = '0'
ceks = 'Iepirkšanās čeks:' #izveidots, lai nav daudz jāraksta teksts.
summa_bez_atlaides = 0.0
kopsumma = 0.0 #galējā summa

while stop == '0':
    ceks
    
    pskaits=int(input('ievadi preču skaitu:'))
    if pskaits < 0:
        exit()
    produkts = input('ievadiet preces nosaukumu: ')
    pcena = round(float(input('ievadiet cenu šai precei: ')),2)  #formatē ar 2sk aiz komata
    
    #atbildes var izvēlēties, ierakstot skaitli no 1 līdz 5
    print('\n1-maxima: 30%atlaide\n2-elvi:40%atlaide, ja klienta karte\n3-Rimi:20%, bet 50%, ja klienta karte\n4-mego:30%, ja pērk 3 un vairāk preces\n5-Aibe:katra otrā par brīvu')
    atlaides_veids=(input('ievadi, kurā veikalā pirksies(rakstiet ciparu no 1 līdz 5): '))
    cena_bez_atlaides = pcena*pskaits #iegūst cenu bez atlaides
    pirkuma_cena = cena_bez_atlaides #no pirkuma cenas rēķinās atlaides

    #sākas atlaižu aprēķināšana
    if atlaides_veids== '1': #atlaide maximā
        #pirkuma_cena= pirkuma_cena*0.7
        pirkuma_cena*=0.7 #izmanto salikto operatoru

    elif atlaides_veids== '2': #atlaide elvi
        elvikarte = input('vai jums ir klienta karte?(1, ja ir,bet2, ja nav) : ')
        if elvikarte=='1':
            pirkuma_cena*=0.6 #atlaide 40%
    elif atlaides_veids=='3':
        rimikarte= input('vai jums ir rimi karte?(1, ja ir,bet2, ja nav)')
        if rimikarte =='1':
            pirkuma_cena*=0.5
        else:
            pirkuma_cena*=0.8
    elif atlaides_veids == "4":
        if pskaits >=3:
            pcena*=0.7

    elif atlaides_veids == '5':
        if pskaits%2==0:
            pirkuma_cena/=2
        else:
            #atņem 1 gb ceno no kopējās
            pirkuma_cena -= pcena
            pirkuma_cena/=2
            pirkuma_cena+=pcena
    cena_bez_atlaides = round(cena_bez_atlaides,2)
    pirkuma_cena = round(pirkuma_cena,2)
    summa_bez_atlaides += cena_bez_atlaides
    kopsumma+=pirkuma_cena
    ceks += produkts+'\n'+str(pcena)+'X'+str(pskaits)+str(cena_bez_atlaides)+'\nAratlaidi:'+str(pcena)
    stop = input('viss nopirkts? j/n  ')
    ceks+=f'kopā bez atlaides(EUR):\t{summa_bez_atlaides}\nKopā ar atlaidēm(eur):\t\t{kopsumma}\n\n'
    print(ceks)
    