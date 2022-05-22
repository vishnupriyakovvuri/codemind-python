n=int(input())
for i in range(1,n+1):
    for j  in range(1,n+1):
            if i+j==n+1 or j==i:
               print('x',end="")
            else:
                print("0",end="")
    print("")