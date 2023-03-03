i="3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
i=str(i).split('.')
m=i[0]+i[1]
t=int(input())
for i in range(0,t):
    con=0
    k=input()
    k=str(k)
    
    for x in range(0,len(k)):
      if(k[x]==m[x]):
          con+=1    
      else:
          break
    
               
    print(con)            
  