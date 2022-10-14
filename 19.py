def xor(a,b):
    if len(a) != len(b):
        return None 
    xor=[]
    for i in range(len(a)):
        if a[i] == b[i]:
            xor.append(0)
                
        else:
            xor.append(1)
    return xor
