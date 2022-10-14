def inserer(el,pos,tab):
    temp=[]
    for i in range(pos):
        temp.append(tab[i])
    temp.append(el)
    for el in tab[pos:]:
        temp.append(el)
        
    return temp