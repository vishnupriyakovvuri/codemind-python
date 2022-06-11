a=input()
b=[]
k=0
for i in range(len(a)-1,-1,-1):
   if ord(a[0])>=65 and ord(a[0])<=91:
     if i==0:
        p=ord(a[i])
        q=p+32
        b.append(chr(q))
     elif i==len(a)-1:
        p=ord(a[i])
        q=p-32
        b.append(chr(q))
     else:
        b.append(a[i])
   else:
        b.append(a[i])
for i in range(0,len(a)):
    if(a[i]==b[i]):
        k+=1
if k==len(a):
    print('True')
else:
    print('False')
    