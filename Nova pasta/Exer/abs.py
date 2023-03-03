n,m,a,b = map(int,input().split(' '))
if(n%m!=0):
    if(n>m):
        k=n//m
        p1 = (n-m*k)*b
        p2 = (m*(k+1)-n)*a
        if(p1<=p2):
            print(p1)
        else:
            print(p2)
    else:
        if(n*b<=(m-n)*a):
            print(n*b)
        else:
            print((m-n)*a)
else:
    print('0')                            