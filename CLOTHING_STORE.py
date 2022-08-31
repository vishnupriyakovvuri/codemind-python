n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if i not in b:
            b.append(i)
            c+=((a.count(i))//2)
print(c)            