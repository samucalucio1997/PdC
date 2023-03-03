pa=input()
crib=input()
cont=0
while len(crib)<=len(pa):
    
    for i in range(0,len(crib)):
        if(pa[i]!=crib[i]):
            con=1
        else:
            con=0 
            break
    cont=cont+con        
    pa=str(pa[1:len(pa)]) 
       
print(cont)       
        