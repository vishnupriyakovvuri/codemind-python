a=input()
b=[]
c=0
for i in a:
    if i!=" ":
        c+=1
    else:
        b.append(c)
        c=0
b.append(c)
print(max(b))