n=7
for x in range(0,n):
    for y in range(0,n):
        if(x==0 or y==0 or x==y or x==n-1 or y==n-1 or x+y==n-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()
