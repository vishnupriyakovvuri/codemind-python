a=input()
b=''
d={}
e=[]
f=[]
g=[]
p=''
k=0
for i in range(0,len(a)):
    if a[i] not in '0123456789!@#$%^&*()':
        b+=a[i]
        f.append(i)
    else:
        e.append(i)
c=b[-1::-1]
for i in range(0,len(a)):
    if i in f:
        g.append(c[k])
        k+=1
    else:
        g.append(a[i])
for i in g:
    p+=i
print(p)    
