# def bin(num):
#     if num==0:
#        return 0
#     else:
#        return 1 + bin(num//2)

# def qtd_div(num,c):
#    if(num==1):
#       return 1
#    if num%c==0:
#       return 1+qtd_div(num,c-1)
#    else:
#       return qtd_div(num,c-1)



# n=int(input())
# for i in range(n):
#    k=int(input())  
#    m=list(map(int,input().split()))
#    con=0
#    c=0
#    for i in range(len(m)):
#       for j in range(1,len(m)-1):
#          if(m[i]==m[j]):
#             con+=m[i]
#    for i in range(len(m)):
#       c+=1 
#    if(c>con): print(con)
#    else: print(c)   

# def Isorder(l):
#    if len(l)==0:
#       return True
#    if l[-1]>=l[len(l)-2]:
#       return Isorder(l[:-1])                 
#    else:
#       return False 
# print(Isorder(l))  

# def ind(l):
#    l2=l.copy()
#    l.sort()
#    if l[-1]<0:
#       return -1
#    else:
#       return l2.index(max(l2))
   

# def poli(coef,x):
#     if len(coef)==1:
#         return coef[-1]
#     else:
#         return x*poli(coef[:-1],x)+coef[-1]


# def div(n,d):
#     if d==1:
#         return [1]
#     lista = div(n,d-1)
#     if n%d==0:
#         lista.append(d)
#         return lista
#     else:
#         return lista

# def Comb(n,k):
#     if n==k:
#         return 1
#     if k==1:
#         return n
#     else:
#         return Comb(n-1,k-1)+Comb(n-1,k)
   
# def pali(l):
    # if len(l)==0 or len(l)==1:
        # return 'é palindromo'
    # if l[-1]==l[0]:
        # return pali(l[1:-1])
    # else: return 'não é palindromo'       
# def inv(l):
#     if len(l)==0:
#         return l
#     if len(l)!=0:
#      x=l[0]
#      l[0]=l[-1]
#      l[-1]=x
#      trocar=inv(l[1:len(l)-1])
#      return l

# def fib(n):
#     if n==0:
#         return 1
#     if n==1:
#         return 1
#     else:
#         return fib(n-1)+ fib(n-2)
    
def ordL(l1,l2):
    if len(l1)==0:
        return l2
    if len(l2)==0:
        return l1
    lista=ordL(l1[:-1],l2[:-1])
    if len()
        if l2[-1]>lista[-1]:
            l1.append(l2) 
        else:
            l2.append(l1)
 
l=[2,3,7,12,24,29]
a=[1,22,31]
print(ordL(l,a))            