def fib(n):
    a=0
    b=1
    for i in range(2,n):
        c=a+b;
        a=b
        b=c
    return b
n=int(input())
if n==1 :
    print('True')
else:
    for i in range(2,n):
        
        if(n==fib(i)):
            print('True')
            break
    else:
        print('False')
        