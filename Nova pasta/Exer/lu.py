'''
n=int(input())
con=1
s=0
for x in range(n):
    if(n%con==0):
        s=s+1
    con=con+1                       
if(s==2):
    print('Sim')
else:
    print('Nao')            
'''
'''
l=[]
a,b,c,d=map(int,input().split(' '))
while a!=0 or b!=0 or c!=0 or d!=0:
    if(a>c or (a==c and d<=b)):
      t=1440-(60*a+b)+c*60+d
      l.append(t)
    else:
            t= c*60+d - (a*60+b) 
            l.append(t)
    a,b,c,d=map(int,input().split(' '))

tam=0
while tam<len(l):
    print(l[tam])
    tam=tam+1
'''
'''
n=int(input())
for x in range(1,n+1):
    if(n%x==0):
        print(x, end=' ')
'''  

'''
n=int(input())
s=0
for x in range(1,n+1):
    s+=1/x
print(f'{s:.4f}')       
'''  
    
