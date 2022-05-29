n=5
n1=0
n2=1 
r=n1+n2
for x in range(1,n+1):
    for y in range(1,x+1):
        print(str(r)+'',end='')
        r=n1+n2
        n1=n2
        n2=r
        
    print()
    
