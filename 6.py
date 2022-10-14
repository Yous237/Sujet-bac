def maxi(tab):
    max=(tab[0],0)
    for el in tab:
        for i in tab:
            if el > i:
                max=(el,tab[el])
    return max
                
                
    
    