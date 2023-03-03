a,b,c =map(int, input().split(' '))
if(a+b>c and a+c>b and b+c>a):
    if((a*a == b*b + c*c) or (b*b == c*c+a*a) or (c*c == a*a + b*b)):
        print('r')
    elif((a*a>=b*b+c*c) or (b*b>=c*c+a*a) or(c*c>=a*a + b*b)):
     print('o')                         
    elif((a*a<=b*b + c*c) or (b*b<=a*a + c*c) or (c*c<=a*a+b*b)):
        print('a')
else:
    print('n')            