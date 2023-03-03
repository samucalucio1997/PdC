test = int(input())

for i in range(0,test):
    b=float(input())
    con=0     
    while b>1:
     b=b/2 
     con+=1
     if(b<1): 
        y=str(con) + ' dias'
        print(y)
     else:
        continue  
     
     
  