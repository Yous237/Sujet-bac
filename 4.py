def recherche(tab):
    rech=[]
    for el in tab:
        for i in tab:
            if i == el+1 or i== el+1:
                couple=(i, el)
                rech.append(couple)
    return(rech) 
            
        
    