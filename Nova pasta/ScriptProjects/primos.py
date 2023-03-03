def  primos(n,d):
    if(d==1):
        return True
    if(n%d==0):
        return False
    else:
        return primos(n,d-1)
    
    
def primo(n):
    if n==1: return False 
    else: return primos(n,n-1) 
    
    

def lista_primos(lista):
    if(len(lista)==0):
        return []
    
    primos=lista_primos(lista[:-1])
    if(primo(lista[-1])):
     primos.append(lista[-1])
    return primos
 
       
'''
y=[1,2,3,4,5,6,7,8,9,11]

print(lista_primos(y))
'''        
def soma_pares(lista):
      if(len(lista)==0):
          return 0
      p=lista[-1]
      n1=soma_pares(lista[:-1])
      if(p%2==0):
          return p+n1
      else:
          return n1


def poli(coef,x):
    if(len(coef)==1):
        return coef[0]
    else:
       return x*poli(coef[:-1],x) + coef[len(coef)-1]


def orde(lista):
    if(len(lista)==0):
        return True
    if(lista[-1]>=lista[len(lista)-2]):
        return orde(lista[:-1])
    else:
        return False


def vezes(lista,x):
    if(len(lista)==0):
        return 0
    if(lista[-1]==x):
        return 1 + vezes(lista[:-1],x)
    else:
        return vezes(lista[:-1],x)
    
'''
y=list(map(int,input().split(' ')))
x=int(input())
print(vezes(y,x))
'''    
def dives(n,d):
    if(d==1):
        return [1]
    else:
      di=dives(n,d-1)
      if(n%d==0):
        di.append(d)
      return dives  
    

def divisores(n):
    return dives(n,n)

def maior(lista):
    if(len(lista)==1):
        return lista[0]
    div=maior(lista[:-1])
    if(lista[-1]>=maior(lista[:-1])):
      div = lista[-1]
    return div


def troca(lista):
    if(len(lista)==0):
        return lista  
    
    
    trocar=troca(lista[1:len(lista)-1])
    if(len(lista)!=0):
     x=lista[0]
     lista[0]=lista[len(lista)-1]
     lista[len(lista)-1]=x
     return trocar
        

   


def palin(lista):
    if(len(lista)==1):
        return 'palindromo'
    if(len(lista)==2):
        if(lista[0]==lista[-1]):
            return 'palindromo'
        else:
            return 'não palindromo'
    k=palin(lista[1:len(lista)-1])    
    if(len(lista)!=2):
        if(lista[0]==lista[-1]):
            return k
        else:
            return 'não palindromo'
        


def divisores(n,d):
    if(n==1 or d==1):
        return [1]
    divi=divisores(n,d-1)
    if(n%d==0):
        divi.append(d)
    return divi 

def divs(n):
    if(n==1):
        return [1]
    return divisores(n,n)
'''u=divs(24)
print(u)      
'''
def merge(l1,l2):
    if(len(l1)==0):
        return l2
    if(len(l2)==0):
        return l1
    if(l1[-1]>=l2[-1]):
        d=merge(l1[:-1],l2)
        return d.append(l1[-1])
    else:
        k=merge(l1,l2[:-1])
        return k.append(l2[-1])
        
        
l1=[1,2,3,4]
l2=[45,56,59,61,72,77] 
w=merge(l1,l2)
print(w)       