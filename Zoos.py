a=input()
c=0
for i in a:
    if 2*a.count('z')==a.count('o'):
        c=1
        break
if c==1:
    print('Yes')
else:
    print('No')