a,b = map(int, input().split(' '))
if(a==1):
    p=b*4
elif(a==2):
    p=b*(4.5)
elif(a==3):
    p=b*5
elif(a==4):
    p=b*2
elif(a==5):
    p = b*(1.5)

print(f'Total: R$ {p:.02f}')            
        