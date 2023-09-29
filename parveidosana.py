#int pārveidošana par str
a = 5 
b = 7
print('skaitlis:',a + b)
print('Teksts',str(a)+str(b)) #concat metode

#izveidot 2 str tipa mainīgos (vērtības '123' un '456')
#pārveidot šos par int tipu

r = '123'
o = '456'
g = int(r)
q = int(o)
print(g+q,type(q+g))