a=input()
b=''
c=''
k=0
for i in a:
    if i in 'aeiouAEIOU':
        b+=i
b=b[-1: :-1]
for i in a:
    if i in 'aeiouAEIOU':
        c+=b[k]
        k+=1
    else:
        c+=i
print(c)        