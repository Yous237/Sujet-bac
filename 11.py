def recherche(tab,n):
    for i in range(len(tab)):
        if tab[i] == n:
            return i
    return -1