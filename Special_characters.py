a=input()
c=0
e=[]
o=[]
k=[]
s=''
for i in a:
    if i in '!@#$%^&*()':
        c+=1
    if i in '1234567890':
        if int(i)%2==0:
            e.append(i)
        else:
            o.append(i)
if c%2==0:
    if(len(e)<=len(o)):
           for i in range(len(e)):
               k.append(e[i])
               k.append(o[i])
           for i in range(len(e),len(o)):
               k.append(o[i])
    else:
           for i in range(len(o)):
               k.append(e[i])
               k.append(o[i])
           for i in range(len(o),len(e)):
                k.append(e[i])           
else:
    if(len(e)<=len(o)):
           for i in range(len(e)):
               k.append(o[i])
               k.append(e[i])
           for i in range(len(e),len(o)):
               k.append(o[i])
    else:
           for i in range(len(o)):
               k.append(o[i])
               k.append(e[i])
           for i in range(len(o),len(e)):
                k.append(e[i])               
for i in k:
    s+=i
print(s)    