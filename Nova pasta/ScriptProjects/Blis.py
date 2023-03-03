
a,b=map(int,input().split())
if(a>=b): c=a
else:   c=b
mdc=1    
for i in range(1,c+1):
    if(a%i==0 and b%i==0):
        a=a/i
        b=b/i
        mdc*=i
                 
print(mdc)             

