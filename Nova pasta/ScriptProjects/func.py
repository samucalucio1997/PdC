def fy(l,a):
    nl = l.copy()
    nl[0]=a
    
    return nl

def fat(a):
    if(a==0):
     return 1
    else:
        return a*fat(a-1) 

def exp(b,l):
    if(l==0):
        return 1
    else:
        return b*exp(b,l-1)
    
def ant(num):
    if(num==1):
        return 1
    else:
     print(num) 
     return ant(num-1)   
    
def div(a,n):
    if(n==1 or a==1):
        return 1   
    if(a%n!=0):
        return div(a,n-1)
    if(a%n==0):
        return 1 + div(a,n-1)


k=div(24,24)
print(k)