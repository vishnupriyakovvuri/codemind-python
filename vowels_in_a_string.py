a=input()
b=input()
k=0
for i in range(len(a)):
    if(a[i]==b):
        k=1
        print('True')
        print(i)
        break
if k==0:
    print('False')

