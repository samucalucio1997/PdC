T= float(input())
if(T>=100 and T<200):
    T=T*(0.9)
elif(T>=200 and T<300):
    T=T*(0.8)
elif(T>=300 and T<400):
    T=T*(0.7)
elif(T>=400 and T<500):
    T=T*(0.6)
elif(T>=500):
    T=T*(0.5)    
else:
    T=0    
print(f'a é {T:02d} de teco {5:02d}')               