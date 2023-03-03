def todas_apagadas(l):
    for lamp in l:
        if lamp==1:
            return False
    return True
 
n,m = map(int, input().split())
lamp = [0]*m
acesas = list(map(int, input().split()))
for i in range(1,len(acesas)):
    lamp[acesas[i]-1] = 1
lamp_inicial = lamp.copy()
interruptores = []
for _ in range(n):
    interruptor = list(map(int, input().split()))
    interruptores.append(interruptor[1:])
cont = 0
while not todas_apagadas(lamp):
    for outrosinterrup in interruptores:
        cont+=1
        for l in outrosinterrup:
            lamp[l-1] = 1-lamp[l-1]
        if(todas_apagadas(lamp)):
            break
    if lamp==lamp_inicial:
        break
if todas_apagadas(lamp):
    print(cont)
else:
    print(-1)