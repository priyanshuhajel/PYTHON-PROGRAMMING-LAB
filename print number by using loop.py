n=5
for x in range(n,0,-1):
    for y in range(n,0,-1):
        if(x==y or x+y==n+1):
            print(x,end='')
        else:
            print('',end='')
        print()
