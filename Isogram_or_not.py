a=input()
c=[]
for i in a:
    if i not in c:
        c.append(i)
if len(a)==len(c):
    print('True')
else:
    print('False')