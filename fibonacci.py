def fib(n):
    a=0
    b=1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(2,n):
        c=a+b;
        a=b
        b=c
        print(b,end=" ")
n=int(input())
fib(n)