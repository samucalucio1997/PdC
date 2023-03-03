t=int(input())
for num in range(0,t):
    pa,pb,g1,g2=map(float, input().split())
    cont=0
    pa=int(pa)
    pb=int(pb)
    while pa<=pb:
        pa=int(pa + (pa*g1)/100)
        pb=int(pb + (pb*g2)/100)
        cont+=1
        if(cont>100 and pa>pb) :
            print('Mais de 1 seculo.')
        elif(pa>pb):
            print(cont, " anos.")            
        