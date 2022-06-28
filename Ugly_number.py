def ugly(n):
    if(n==1):
        return 1
    elif(n%2==0):
        return ugly(n//2)
    elif(n%3==0):
        return ugly(n//3)
    elif(n%5==0):
        return ugly(n//5)
    else:
        return 0
a=int(input())
if(ugly(a)==1):
    print('Ugly Number')
else:
    print('Not Ugly Number')