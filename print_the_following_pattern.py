n=int(input())
c=65
for i in range(1,n+1):
    for j  in range(1,n+1):
        print(chr(c),end=" ")
    c=c+1
    print("")