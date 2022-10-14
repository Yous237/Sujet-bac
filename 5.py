def rechercheminmax(tab,minmax = {min: 0,max: 0}):

    if tab == None:
        return None
    else:
        if tab == None:
            return minmax
        else:
            if tab[0] < minmax[min]:
                return rechercheminmax(tab[:1],minmax={min:tab[0] ,max: ""})
            elif tab[0] >minmax[max]:
                return rechercheminmax(tab,minmax={min:"" ,max:tab[0]})
            else:
                return rechercheminmax(tab[:1],minmax={min:"" ,max: ""})
            
