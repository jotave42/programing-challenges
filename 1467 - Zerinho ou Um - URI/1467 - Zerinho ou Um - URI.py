import sys
for ent in sys.stdin:
    ent=ent.split(" ")
    a=ent[0]
    b=ent[1]
    c=ent[2]
    c=c.replace("\n","")
    if a==b and b==c:
        print("*")
    elif a==b and b!=c:
        print("C")
    elif a==c and b!=c:
        print("B")
    else:
        print("A")
