import sys
total=0
retornaram=0
for ent in sys.stdin:
    ent = ent.replace("\n", "")
    if total==0 and retornaram==0:
        ent = ent.split(" ")
        total=int(ent[0])
        retornaram=int(ent[1])
    else:
        if total== retornaram:
            print("*")
        else:
            ent = ent.split(" ")
            res=""
            for i in range(1,int(total)+1):
                tempi=str(i)
                if ent.count(tempi)<=0:
                    res+=tempi+" "
            print(res)
        total=0
        retornaram=0
