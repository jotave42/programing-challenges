import math
import sys
for ent in sys.stdin:
    ent=ent.split(" ")
    dfg=int(ent[0])
    vf=int(ent[1])
    vg=int(ent[2])
    dg= math.sqrt(144+(dfg**2))#144=12^2 12 é a distancia da fugitivo para escapar
    tf=12/vf#t=d/v d=12
    tg=dg/vg
    if(tg<=tf):
        print("S")
    else:
        print("N")




































