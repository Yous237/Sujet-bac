def recherche(elt,tab):
    compt=0
    for i in range(len(tab)):
        if tab[i]==elt:
            return i
        return -1



def ins(el, tab):
    for n in range(len(tab)):
        if el > tab[n]:
            pos=tab[n]
    temp=[]
    for i in range(pos):
        temp.append(tab[i])
    temp.append(el)
    for el in tab[pos:]:
        temp.append(el)
    return temp

            


            
            