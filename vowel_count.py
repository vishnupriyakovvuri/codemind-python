a=input()
b=[]
c=['a','e','i','o','u']
k=0
for i in a:
    if i in 'aeiouAEIOU':
            k+=1
if k==0:
    print('0')
else:
    print(k)
