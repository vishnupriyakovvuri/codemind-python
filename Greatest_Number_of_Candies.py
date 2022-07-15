n=int(input())
a=list(map(int,input().split()))
m=int(input())
for i in a:
    if(i+m>=max(a)):
        print('True',end=" ")
    else:
        print('False',end=" ")