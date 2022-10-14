def multiplication(a,b):
    if a < 0 and b < 0:
        return 0
    s=0
    for i in range(a):
        print(b)
        s=s+b
    return s

def dichotomie(tab,x):
    for el in tab:
        if el == x:
            return True
    return False 