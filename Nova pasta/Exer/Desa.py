n=int(input())
for i in range(n):
    a,b=map(int, input().split())
    k=input()
    d=input()
    if(k[-1]==d[-1] and (d[len(d)-2]==d[-1]) and (k[len(k)-2]==k[-1])):
      p='NO'
      print(p)
      break
    else:
        p='YES'
    tam=len(k)
    tm=len(d)
    if tam<tm:
        while tm>=3:
            if d[-1]==d[tm-2] and d[tm-2]==d[tm-3]:
                p='NO'
                tm-=1
                print(p)
                break
            else:
                tm-=1
                continue
    else:
        while tam>=3:
            if k[-1]==k[tm-2] and k[tm-2]==k[tm-3]:
                p='NO'
                tam-=1 
                print(p)      
                break
            else:
                tam-=1
                continue
    print(p)        