t=int(input())
for i in range(t):
    a=input()
    b=a[-1: :-1]
    f=0
    for i in range(len(a)):
        if(a[i]!=b[i]):
           f=1
    if(f==0):
         if(len(a)%2==0):
            print('YES','EVEN')
         else:
             print('YES','ODD')
    else:
          print('NO')