def pali(x):
    p=0
    while x!=0:
        r=x%10
        p=p*10+r
        x=x//10
    return p
a=int(input())
q=pali(a)
a=a+q
while (a!=pali(a)):
    a+=pali(a)
print(a)    