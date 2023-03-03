a,b,c = map(int, input().split(' '))
x,y,z = map(int, input().split(' '))
e1 = x-a
e2 = y-b
e3 = z-c
if(e1<0 and e2>0 and e3>0):
    s=e2+e3
    print(s)
elif(e1>0 and e2>0 and e3>0):
    s=e1+e2+e3
    print(s)
elif(e1==0 and e2==0 and e3==0):
    s=0
    print(s)
elif(e1>0 and e2<0 and e3>0):
    s=e1 + e3
    print(s)
elif(e1<0 and e2<0 and e3>0):
    s=e3
    print(s)
elif(e1>0 and e2>0 and e3<0):
    s=e1+e2
    print(s)
elif(e1<0 and e2<0 and e3<0):
    s=0
    print(s)
elif(e1<0 and e2>0 and e3<0):
    s = e2
elif(e1>0 and e2<0 and e3<0):
    s=e1
    print(s)