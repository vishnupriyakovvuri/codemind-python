a=input()
b=input()
d=a.lower()
e=b.lower()
c=[]
k=0
if len(d)==len(e):
    for i in range(len(d)):
          for j in range(len(e)):
            if d[i]==e[j]:
                if i not in c:
                    c.append(e[j])
                    k+=1
    if k==len(d):
        print('True')
    else:
        print('False')
else:
    print('False')