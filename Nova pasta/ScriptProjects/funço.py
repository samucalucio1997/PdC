
def fat(a):
    if(a==0):
        return 1
    else:
        return a*fat(a)


def inver(lista):
   lista.reverse()
   return lista    

def contarP(a):
    if(a==a):
        return a
    else:
        return a + contarP(a) 
        
        
def fib(a):
   if(a==0 or a==1):
        return 1
   else:
        return fib(a-2) + fib(a-1)
    
def PA2(i):
    if (i==1):
        return 2
    else:
        return PA2(i-1) + 2    
    
def SPA2(i):
    if(i==1):
        return 2
    if(i>1):
        return  SPA2(i-1) + PA2(i)
    
def PG2C(i):    
       if(i==1):
           return 2
       else:
           return 2*PG2C(i-1)   
                
def SP2(i):
    if(i==1):
        return 2 
    else:
        return SP2(i-1)+PG2C(i) 
    
y=SP2(4)
print(y)    

def f(x,y):
  if (y==0):
   return 0
  else:
   return x + f(x,y-1)
      
m=f(2,5)
print(m)    
