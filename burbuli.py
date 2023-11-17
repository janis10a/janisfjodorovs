#merkis ir uztaisit burbulu spridzinataju


from random import *
from tkinter import *
from math import *

logs = Tk()
garums = 700
platums = 700
logs.title('Burbuļu spridzinātājs')
a=Canvas(logs, width=platums, height=garums,bg='pale green')
a.pack()
kuga_id2 = a.create_oval(10,10,80,80,outline='purple', width=10)


mainloop()