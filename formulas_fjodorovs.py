import math
import random
radiuss = float(input('ievadied rinķa līnijas rādiusu:'"\n"))
print(radiuss)
rlg = 2*math.pi*radiuss
print("rinķa līnijas garums:","{:.2f}".format(rlg))
rll = math.pi*radiuss**2
print("{:.2f}".format(rll))
katete1 = float(input ("ievadiet taisnlenķa trijstūra pirmās katetes garumu:"'\n'))
katete2 = float(input('ievadiet taisnlenķa trijstūra otrās katetes garumu:''\n'))
hipotenuza = math.sqrt(katete1**2+katete2**2)
print('taisnlenķa trijstūra hipotenūzas garums:',"{:.2f}".format(hipotenuza))
cipars = random.random()
print('gadījuma skaitlis no 0 - 1:',cipars)
