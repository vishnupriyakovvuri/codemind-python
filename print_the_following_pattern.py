n=int(input())
for i in range(1,n+1):
    for j  in range(1,n+1):
        if i<n:
            if j==1 or j==i:
               print('*',end="")
            else:
                print(" ",end="")
        else:
            print("*",end="")
            
    print("")