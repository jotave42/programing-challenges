import math
import sys
for str in sys.stdin:
    str=str.split(" ")
    dfg=int(str[0])
    vf=int(str[1])
    vg=int(str[2])
    dg= math.sqrt(144+(dfg**2))#144=12^2 12 é a distancia da fugitivo para escapar
    tf=12/vf#t=d/v d=12
    tg=dg/vg
    if(tg<=tf):
        print("S")
    else:
        print("N")




































