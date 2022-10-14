def nb_repetitions(n,tab):
    compt=0
    for el in tab :
        if n == el:
            compt+=1
    return compt


def bina(a):
    bina=""
    while a >=1:
        if a % 2 == 0:
            bina=  "0" + bina 
            a = a//2
        else :
            bina = "1" + bina
            a = a//2
    return bina 
            
        