n=int(input())
for i in range(1,n+1):
    for j in range (1,n+2-i):
        print("%c"%chr(65+n-i),end=" ")
    print()        