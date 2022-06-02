n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
b.extend(a)
a.sort(reverse=True)
for i in range(len(a)):
    for j in range(i,i+1):
        if a[i]==b[j]:
           c+=1
if c==len(a):
    print('yes')
else:
    print('no')
 