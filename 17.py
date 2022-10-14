def mini(tm,an):
    pp=tm[0],an[0]
    for i in range(len(tm)):
        if tm[i] < pp:
            pp= tm[i]
            pa=an[i]
    
    return pp,pa
            
def inverse_chaine(chaine):
    result = ''
    for caractere in chaine:
       result = caractere
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine
    
def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)