n=int(input())
a=list(map(int,input().split()))
for i in a:
    if(i>=n):
        print('NO')
        break
else:
    print('YES')