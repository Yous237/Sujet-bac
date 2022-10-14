
def calcul(n,un=[]):
    
    if n == 1:
        un.append(1)
        return un
    else:
        un.append(int(n))
        if n%2 == 0:
            return calcul(n/2,un)
        else:
   
            return calcul(n*3 +1,un)
            """
def calcul(n):
    un=[]
    While n =! 1:
        un.append(n)
        if n%2 == 0:
            n= n/2
        else:
            n=n*3 +1
    return un
"""
dico = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, \
 "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, \
 "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, \
 "T":20, "U":21,"V":22, "W":23, "X":24, "Y":25, "Z":26}

def est_parfait(nom):
    lettre=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    code=""
    for let in nom:
        for i in range(len(lettre)):
            if lettre[i] == let:
                code = code + str(i+1)
    return int(code)
        

