n=int(input())
a=list(map(int,input().split()))
b=[ ]
k=0
for i in a:
        if i%2==0:
            if i not in b:
                b.append(i)
                k=k+1
print(k)