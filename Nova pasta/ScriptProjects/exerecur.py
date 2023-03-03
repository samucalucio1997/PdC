def vezes(lista,x):
    if(len(lista)==0):
        return 0
    if(lista[-1]==x):
        return 1+vezes(lista[:-1],x)
    else: return vezes(lista[:-1],x)
        
def to_im(lista):
    if(len(lista)==0):
        return True
    if(lista[-1]%2!=0):
        return to_im(lista[:-1])
    else:
        return False
 
   
def con(n,d):
    if(n//10==0 and n%10==0):
        return 0
    if(n%10==d):
        return 1+con(n//10,d) 
    else:
        return 0 + con(n//10,d)

w=con(16458471244,1)
print(w)
    
 
 