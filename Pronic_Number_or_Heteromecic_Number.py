n=int(input())
for i in range(1,(n//2)+1):
    j=i+1
    if(i*j==n):
        print('YES')
        break
else:
    print('NO')