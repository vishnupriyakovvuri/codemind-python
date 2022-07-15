a=input()
b=input()
c=''
a=list(a+b)
a.sort()
for i in a:
    c+=i
print(c)    