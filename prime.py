a=int(input('enter number :'))
c=0
for i in range(1,a+1):
    if a%i==0:
        c+=1
if c==2:
    print('number is prime')
else:
    print('number is not prime')
    
