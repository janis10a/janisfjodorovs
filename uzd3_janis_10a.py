saraksts = []#uztaisu tukšu sarakstu, kur lietotājs var ievietot vērtības.
daudzums = int(input('ievadiet skaitļu skaitu(ne mazāk kā 3): ')) #uzzinu saraksta garumu
if daudzums>= 3:
    for i in range(daudzums): #for cikls, lai saraksta elementus iegūtu tik reizes, cik nepieciešams.
        elements = input('ievadiet skaitli, kuru vēlaties pievienot: ')
        saraksts.append(elements)#pievieno elementu sarakstam
    print('saraksts ar skaitļiem: ',saraksts)
    print('lielākais ievadītais skaitlis ir: ',max(saraksts))#ar max funkciju atrod lielāko skaitli
    exit()#beidz programmu
else:
    while True:
        daudzums = int(input('ievadiet skaitļu skaitu(ne mazāk kā 3): ')) #iegūst saraksta garumu
        if daudzums>= 3:
            for i in range(daudzums):#for cikls, lai saraksta elementus iegūtu tik reizes, cik nepieciešams.
                elements = input('ievadiet skaitli, kuru vēlaties pievienot: ')
                saraksts.append(elements) #pievieno elementu sarakstam
            print('saraksts ar skaitļiem: ',saraksts)
            print('lielākais ievadītais skaitlis ir: ',max(saraksts))#ar max funkciju atrod lielāko skaitli
            exit()