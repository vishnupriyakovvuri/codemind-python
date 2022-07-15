t=int(input())
for i in range(t):
    a=input()
    for i in a:
        if i in '1234567890':
            print('Yes')
            break
    else:
         print('No')