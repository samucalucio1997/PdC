x,q=input().split(' ')
x = int(x)
q = int(q)

if(x==3):
    t=q*5
elif(x==1):
    t=q*4
elif(x==2):
    t=q*4.5
elif(x==4):
    t=q*2
else:
    t=q*1.5        
    
t = float(t)
print(f'Total: R$ {t:.2f}')