saraksts=[]#uztaisu sarakstu
daudzums = int(input('ievadiet skaitļu skaitu(ne mazāk kā 10): ')) #uzzinu saraksta garumu
if daudzums>= 10:#ja lietotājs ievada derīgu skaitļu skaitu, ko ievietot sarakstā, programma turpinās
    for i in range(daudzums): #for cikls, lai saraksta elementus iegūtu tik reizes, cik nepieciešams.
        elements = int(input('ievadiet skaitli, kuru vēlaties pievienot: '))
        saraksts.append(elements)#pievieno elementu sarakstam
    print('Saraksts: ',saraksts)
    para, nepara = 0,0 #radu vietu, kur glabāt cik pāra un nepāra skaitļi ir sarakstā
    for num in saraksts: #for cikls lai atrastu visus pāra un nepāra skaitļus
        if num % 2 == 0:
            para += 1
        else:
            nepara += 1
    print('pāra skaitļu skaits: ',para)
    print('nepāra skaitļu skaits: ',nepara)
else: #ja ievada nederīgu skaitļu skaitu priekš saraksta,šis aktivizējas, lai beigtu programmu un dotu iemeslu.
    print('skaitļu skaitam sarakstā jābūt vismaz 10')
    exit()#beidz programmu