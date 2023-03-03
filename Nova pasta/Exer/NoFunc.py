def menor(a,b,c):
    menor=a
    if(b<menor):
        menor=b
    if(c<menor):
        menor=c        
    return menor    

def maior(a,b,c):
    maior=a
    if(b>maior):
        maior=b
    if(c>maior):
        maior=c
    return maior  

l,n1,n2,n3=map(int, input().split(' '))
L,a1,a2,a3,a4,a5=map(int, input().split(' '))
B1= 1.5*((n1+n2+n3 - maior(n1,n2,n3)-menor(n1,n2,n3)) + l)/2 
M=[a1,a2,a3,a4,a5]
y=maior(a1,a2,maior(a3,a4,a5))
x=menor(a1,a2,menor(a3,a4,a5))
k=sum(M)
MP=(k-x-y)/3
B2= (L*1.2+1.8*MP)/2
Media = (2*B1+3*B2)/5

if(Media>=60):
    print('Aprovado')
else:
    print('Não Aprovado')    