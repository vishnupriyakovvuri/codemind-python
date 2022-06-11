a=input()
b=[]
k=0
for i in a:
    if i in 'AEIOUaeiou':
        if i not in b:
            b.append(i)
            k+=1
if k==0:
    print(-1)
else:
    for i in b:
        print(i,end=" ")
