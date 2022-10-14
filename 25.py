def selection_enclos(tab,n):
    t=[]
    for el in tab:
        if el['enclos'] == n:
            t.append(el)
    return t

animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
 {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
 {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
 {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
 {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

def trouver_intrus(tab, g, d):
    '''
    Renvoie la valeur de l'intrus situÃ© entre les indices g et d 
    dans la liste tab oÃ¹ 
	tab vÃ©rifie les conditions de l'exercice,
    	g et d sont des multiples de 3.
    
    if g == d:
        return False 
    
    else:
        nombre_de_triplets = (d - g)// ...
        indice = g + 3 * (nombre_de_triplets // 2)
        if ... :
            return ...
        else:
            return ...'''
    compt=0
    for i in range(g,d):
        for z in range(g,d):
           if tab[i] == [z]:
               compt+=1
            
        if compt == 1:
            return tab[i]
                
        else:
            compt=0