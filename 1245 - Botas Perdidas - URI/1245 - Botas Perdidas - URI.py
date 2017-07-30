import sys
esquerda=[]
direita=[]
botas=0
pares=0
for ent in sys.stdin:
    if botas==0:
        botas=int(ent)
        pares=0
    else:
        ent=ent.split(" ")
        if ent[1]=="D\n":
            if esquerda.count(ent[0])>0:
                pares+=1
                esquerda.remove(ent[0])
            else:
                direita.append(ent[0])
        else:
            if direita.count(ent[0])>0:
                pares+=1
                direita.remove(ent[0])
            else:
                esquerda.append(ent[0])
        botas-=1
        if(botas==0):
            esquerda=[]
            direita=[]
            print(pares)
