def listapar(l,a):
    c=0
    k=[]
    while(c<len(l)):
        k.append(a*l[c])
        c+=1
    print(k)     
          
            
lista = list(map(int, input().split(' ')))
a=int(input()) 
l2 = listapar(lista,a) 
print(l2)
        