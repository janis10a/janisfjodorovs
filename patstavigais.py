'''izveidot 3 sarakstus: lietotājs pats noādīs,
 cik elementus likt sarakstā. 
 pirmā un otrā saraksta vērtības ievava lietotājs.
 trešā saraksta vērtības iegūst apienojot pirmos 2 sarakstus
 katra saraksta saturu glīti parādīt uz ekrāna.'''

list1 = []
list2 = []
list3 = []

list1_value = int(input('type the first lists amount of elements: '))
list2_value = int(input('type the second lists amount of elements: '))

for i in range(0,list1_value):
    ele = int(input('input the value: '))
    list1.append(ele)
print(list1)

for i in range(0,list2_value):
    eles = int(input('input the value: '))
    list2.append(eles)
print(list2)

list3 = list1+list2
print('list 1: ',list1,'\n','list 2: ', list2,'\n','list 3', list3)