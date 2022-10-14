def occurence(string):
    dic={}
    for le in string:
        compt=0
        for i in range(len(string)):
            if le == string[i]:
                compt+=1
                if string[i] in dic.keys:
                    compt=compt+1
                    dic[le]=compt
                        
                else:
                    dic[le]=compt
    return dic

def fusion(l1,l2):
    l1=l1+l2
    
    l12=[]
    ppetit1=l1[0]
    while len(l1) !=0:       
        for el in range(len(l1)):
            for i in range(len(l1)):
                if l1[el] < l1[i] and l1[el] < ppetit1:
                    ppetit1=l1[el]
                    
                    
                elif l1[i] < l1[el] and l1[i] < ppetit1:                   
                    ppetit=l1[i]
                    
                   
        l12.append(ppetit1)            
        l1.pop(ppetit1)

    return l12
                
        
    