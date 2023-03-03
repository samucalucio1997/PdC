def div(n,p):
    if(n==1 or p==1):
        return 1
    if(n%p == 0):
        return 1 + div(n,p-1)
    else:
        return 0 + div(n,p-1)
   
def div2(l,n,p):
    if(n==1 or p==1):
        l.append(1)
        return l
    if(n%p==0):
        l.append(p)
        return div2(l,n,p-1)
    else:
        return div2(l,n,p-1)
                    
    
def primo(n):
    p=n
    if(div(n,p)==2):
        return 'primo'
    else:
        return 'não é primo'  


def Comb(n,k):
    if(n==k):
        return 1
    if(k==1):
        return n
    else:
        return  Comb(n-1,k-1) + Comb(n-1,k) 
      
      
def listprim(l,n,p):
    if(primo(l[0])=='primo'):
        print(l[0])
        return p.append(primo(l[0]))
    if(primo(l[n-1])=='primo'):
        p.append(primo(l[n-1]))
        print(p)
        return listprim(l,n-1,p)
    else:
        print(p)
        return listprim(l,n-1,p)
               

def bin(n):
    if(n==1):
        return 1
    else:
        return 1 + bin(n//2)
        
        
def hum(lista):
    x=len(lista)
    if(x==0):
        return True
    elif(lista[x-1]>=lista[x-2]):
        lista.remove(lista[x-1])
        return hum(lista)
    else:
        return False


def joinList(l1,l2,p):
    if(len(l1)==0 and len(l2)==0):
        return p
    if(l2[len(l2)-1]<=l1[len(l1)-1]):
        p.append(l1[len(l1)-1])
        p.append(l2[len(l2)-1])
        l1.remove(l1[len(l1)-1])
        l2.remove(l2[len(l2)-1])
        return joinList(l1,l2,p)
    if(l2[len(l2)-1]>=l1[len(l1)-1]):
        p.append(l1[len(l1)-1])
        p.append(l2[len(l2)-1])
        l1.remove(l1[len(l1)-1])
        l2.remove(l2[len(l2)-1])
        return joinList(l1,l2,p)
    if(len(l1)==0):
         p.append(l2[len(l2)-1])
         l2.remove(l2[len(l2)-1])
         return joinList(l1,l2,p)
    if(len(l2)==0):
        p.append(l1[len(l1)-1]) 
        l1.remove(l1[len(l1)-1])
        return joinList(l1,l2,p)
    
def maior(l):
     if(max(l)==l[len(l)-1]):
         return len(l)-1
     else:
         l.remove(l[len(l)-1])
         return maior(l)
     
def cont(l,x):
    n=l[len(l)-1]
    if(l[n] == x):
        return 1 + cont(l.remove(l[len(l)-1]),x)
    else:
      l.remove(l[len(l)-1])
      return cont(l,x) 
     
     
def listaOrd(l,n,y):
    '''
    n=0
    y=len(l)
    '''
    if(y==len(l)//2):
        return l
    else:     
        x=l[n]
        l[n]=l[y]
        l[y]=x
        return listaOrd(l,n+1,y-1)
        '''
        n=+1
        y=-1
        '''

def pali(l,n,y):
    if(y-n<=2):
        return True
    if(l[n]==l[y]):
        l.remove(l)
        return pali(l,n+1,y-1)
    else:
        return False

def primo2(n,d):
    if(d==1):
        return 'primo'
    if(d!=n and d!=1):
        if(n%d==0):
            return 'não primo' 
        else:
            return primo2(n,d-1)
    else:
        return primo2(n,d-1)
    
def paresum(l,p):
    if(len(l)==0):
        return sum(p)
    if(l[len(l)-1]%2==0):
        p.append(l[len(l)-1])
        l.remove(l[len(l)-1])
        return paresum(l,p)
    else:
        l.remove(l[len(l)-1])
        return paresum(l,p)
    
    
l=[1,11,22,33]       
w=hum(l)
print(w)        