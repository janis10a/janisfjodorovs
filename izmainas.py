saraksts=[1,7,5,6,4,12,9,8]
saraksts.append('Cepums') #pievieno beigās
print(saraksts)

saraksts.pop()#izmet no beigām
print(saraksts)

saraksts.insert(3,'Hello!') #ievieto 3. no kreisās
print(saraksts)

saraksts.remove('Hello!')#izmet norādīto vērtību no saraksta
print(saraksts)

tests = [1,2,3,4,5,6,7,8]
del tests[2] #funkcija delete, izdzēš 1 elementu
print(tests)

del tests[3:6]
print(tests) #izdzēš intervālu

cipari = [1,2,3,4,5,6,7,8]
del cipari [2:7:2]#no 2. indeksa līdz 7. dzēš katru otro
print(cipari)