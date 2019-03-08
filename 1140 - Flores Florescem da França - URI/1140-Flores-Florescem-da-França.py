import sys
def isTautogram(phrase):

    phrase=phrase.lower()
    words =phrase.split()
    letter =words[0][0]
    for i in range(0,len(words),1):
        if(letter != words[i][0]):
            print("N")
            return
    print("Y")
    return
for ent in sys.stdin:
    if (ent[0] == "*") and (len(ent)<=2):
        break
    isTautogram(ent)

