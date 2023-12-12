username='skolens'
password='tikai'
tries=5
user_input=input('lūdzu ievadiet savu lietotājvārdu: ') #pieprasa ievadīt paroli un lietotājvārdu
password_input=input('lūdzu ievadiet savu paroli: ')
if user_input==username and password_input==password:  #pārbauda vai parole un lietotājvārds ir pareizi
    print('pieslēgšanās veiksmīga')
    first_number=int(input('ievadiet 1. veselo skaitli: '))
    second_number=int(input('ievadiet 2. veselo skaitli: ')) #pieprasa abus skaitļus
    res=[]
    for i in range(first_number,second_number,1):
        totalsum=sum(i)
        print('Veselu secīgi pieaugošu skaitļu summa no ',first_number,' līdz ',second_number,' ir: ',totalsum)
        if first_number or second_number == 'stop':
            print('programma beidzas.')
            

elif user_input!=username or password_input!=password:  #
    while tries!= 0:
        user_input=input('lūdzu ievadiet savu lietotājvārdu: ')
        password_input=input('lūdzu ievadiet savu paroli: ')
        if user_input==username and password_input==password: #ja parole tagad pareiza, laiž programmā
            print('pieslēgšanās veiksmīga')
            first_number=int(input('ievadiet 1. veselo skaitli: '))
            second_number=int(input('ievadiet 2. veselo skaitli: ')) #pieprasa abus skaitļus
            res=[]
            for i in range(first_number,second_number,1):
                totalsum=sum(i)
                print('Veselu secīgi pieaugošu skaitļu summa no ',first_number,' līdz ',second_number,' ir: ',totalsum)
                if first_number or second_number == 'stop':
                    print('programma beidzas.')
        elif user_input!=username or password_input!=password:
            tries=tries-1
            print('jums ir atlikuši ',tries,' mēģinājumi!')
            if tries == 0:
                print('jums ir beigušies mēģinājumi, prgramma beidzas.')