def area(c,l):
    
   return c*l
    
    
def maior(a,b,c,d):
    maior=a 
    y='A'
    if(b>maior):
        maior=b
        y='B'
    if(c>maior):
        maior=c 
        y='C'
    if(d>maior):
        maior=d
        y='D'
    return y
              
           
a,b = map(int, input().split(' ')) 
c,d = map(int, input().split(' ')) 
e,f = map(int, input().split(' ')) 
g,h = map(int, input().split(' '))

x=area(a,b)
y=area(c,d)
z=area(e,f)
w=area(g,h) 

t=maior(x,y,z,w) 
print(t)         
           