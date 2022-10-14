def rendu(n):
    n1= n / 5
    n2= (n%5) / 2
    if n2 % 2 != 0:
        return [int(n1),int(n2),1]
    return [int(n1),int(n2),0]