x = int(input())
print(x)
y = x/100
print(str(int(y)) + " nota(s) de R$ 100,00")
z=x%100
cinq=z/50
print(str(int(cinq))+ " nota(s) de R$ 50,00")
r = z%50
rest = r/20
print(str(int(rest))+ " nota(s) de R$ 20,00")
r2 = r%20
la = r2/10
print(str(int(la))+" nota(s) de R$ 10,00")
r3 = r2%10
un1 = r3/5
print(str(int(un1))+" nota(s) de R$ 5,00")
reu1 = r3%5
un2 = reu1/2
print(str(int(un2))+" nota(s) de R$ 2,00")
reu2 = reu1%2
print(str(int(reu2))+" nota(s) de R$ 1,00")
    
 
