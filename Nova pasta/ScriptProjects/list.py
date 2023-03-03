tests = int(input())
for i in range(0,tests):
 a,b,c,d=map(float, input().split(' '))
 a=int(a)
 b=int(b)
 con=0  
 while b>=a:
     a=int(a+(c*a)/100)
     b=int(b+(b*d)/100)
     con+=1  
     if(con>100):
      print('Mais de 1 seculo.')
      break
     else: 
      t=str(con)         
      print(t +' anos.') 

   
   
    