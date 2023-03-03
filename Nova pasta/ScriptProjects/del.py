a,b,c = map(int, input().split(' '))
s1 = a+b
s2 = a+c
s3 = b+c
if(s1<s2 and s1<s3):
    if(s1<=c):
        print('nao maior')
    else:
        print('maior')
elif(s2<s1 and s2<s3):
    if(s2<=b):
        print('nao maior')
    else:
        print('maior')
elif(s3<s1 and s3<s2):
    if(s3<=a):
        print('nao maior')
    else:
        print('maior')    
                                