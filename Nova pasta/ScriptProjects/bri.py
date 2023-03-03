a,b = map(int, input().split(' '))
if(b>a):
    d=b-a
    if(d%2==0):
        a=a+(d-1)+3
        s=1
        a=a-2
        s=s+1
        print(s)
    elif(d%2!=0):
        a=a+d
        s=1  
        print(s) 
    elif(d==0):
        s=0
        print(s)
elif(b<a):
    d=a-b
    if(d%2==0):
        a=a-d
        s=1
        print(s) 
    elif(d%2!=0):
        a=a-(d+1)
        s=1
        a=a+1
        s=s+1
        print(s) 
elif(a==b):
    print('0')                     
               
        