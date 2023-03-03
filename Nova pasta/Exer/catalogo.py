lista=list(map(int, input().split(' ')))
x=len(lista)
y=x//2
if(x%2==0):
    print('Não existe termo central')
else:
    print(lista[y])    