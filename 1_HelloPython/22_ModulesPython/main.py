#module - a file containing python code. May contain functions, classes, etc.
#         used with modular programming, which is to separate a program into parts

import messeges as mes
print("--messeges as mes--")
mes.hello()
mes.bye()
mes.good()


import messeges
print("\n--messeges--")
messeges.hello()
messeges.bye()
messeges.good()


from messeges import hello ,bye
hello()
bye()
#good()         #jest to źle ponieważ importujemy tylko 2 metody

from messeges import *

hello()
bye()
good()     #tu zadziała ponieważ gwiazdka pozwala na import wszytskich metod z pliku
