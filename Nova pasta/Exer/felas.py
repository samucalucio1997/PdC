n=int(input())
for i in range(2,n):
    if(n%i==0 or n==2 or n==1):
        k='não é primo'
        break
    else:
        k='é primo'
        continue

print(k)           