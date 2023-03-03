a,b,c = map(int, input().split(' '))
if(a<28 and b<=12):
     print('valida')
elif(a==28 and b==2):
     print('valida')
elif(a==30 and (b==4 or b==6 or b==9 or b==11)):
     print('valida') 
elif(a==31 and (b==1 or b==3 or b== 5 or b==7 or b==8 or b== 10 or b==12)):
     print('valida')
else:
    print('invalida')                 