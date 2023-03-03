def conta_digito(x,d):
    if(x==0):
        return 0
    if(x%10==d):
        return 1 + conta_digito(x//10,d)
    else:
        return 0 + conta_digito(x//10,d)

def sum(n):
    if(n==1):
        return 1
    else:
        return n + sum(n-1)

def div(m,n):
    if(m==0 or m<n):
        return 0
    else:
        return 1+div(m-n,n)
    
def alg(n):
    if(n//10==0):
        return n
    else: return alg(n//10)    

def num(n):
    if(n//10==0):
        return 1
    else:
        return 1+num(n//10)
    
def soma_alg(n):
    if(n//10==0):
        return n 
    else:
        return n%10 + soma_alg(n//10)    
    
def medialg(n):
    if(n//10==0):
        return n
    else: return soma_alg(n)/num(n)
    
def imaior(lista):
    if(len(lista)==1):
        return 0
    u=lista[-1]
    inmaior=imaior(lista[:-1])
    if(lista[-1]>=inmaior):
        inmaior=lista.index(u)
        return inmaior  
    else: return inmaior  

l=[1,2,4,45,6,7]
w=imaior(l)
print(w)    