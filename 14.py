def correspond(mot,mat):
    if len(mot) < len(mat) or len(mot) > len(mat):
        return False
    elif mot == "":
        return True
    else:
        if mot[0] == mat[0]:
            return correspond(mot[1:],mat[1:])
        elif mat[0] == '*':
            return correspond(mot[1:],mat[1:])
            
        
        else:
            return False
        
        
def 
                              