a=input()
b=[]
c=['a','e','i','o','u']
k=0
for i in a:
    if i in 'aeiou':
        if i not in b:
            b.append(i)
for i in b:
    if i  in c:
        k+=1
if k==5:
    print('True')
else:
    print('False')
    