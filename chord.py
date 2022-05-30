n=5
for x in range(1,n+1):
    d=n-x
    for y in range(1,n+1):
        print(chr(d+65)+'',end='')
        d=d+n
    print()
    
