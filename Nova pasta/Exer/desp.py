l=[1,22,4,31,9,50,21]
l.sort()
print(l)

l2 = sorted(l)
y=l[4]
l[5]=l[2] + y
l2.insert(2,l[5])
print(l2)
print(l2.index(31))
l3=l[2:6]
print(l3)
x=7
print(x)
l.append(x)
print(l)