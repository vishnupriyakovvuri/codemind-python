t=int(input())
for j in range(t):
    n=int(input())
    a=input()
    c=0
    for i in a:
        if a.count(i)==1:
            print(i)
            c=1
            break
    if(c==0):
        print('-1')