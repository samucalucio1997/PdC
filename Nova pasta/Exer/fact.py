def fat(a):
    if(a==0):
      return 1
    else:
        return a*fat(a-1)
    
a,b=map(int,input().split(' '))    
    
print(fat(a) + fat(b))    