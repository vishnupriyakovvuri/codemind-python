a=input()
b=[]
c=['a','e','i','o','u']
k=0
for i in a:
    if i in 'aeiou':
        if i not in b:
            b.append(i)
for i in c:
    if i not in b:
        print(i,end=" ")
        k+=1
if k==0:
    print('0')