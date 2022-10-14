def moyenne(tab):
    somme=0
    if tab == None:
        return 'erreur'
    for el in tab:
        somme = somme + el
    return somme/len(tab)

def tri(tab):
    tabtri=[]
    
    for el in tab:
        if el == 0:
            tabtri.append(0)
    for ele in tab:
        if ele == 1:
            tabtri.append(1)
    return tabtri