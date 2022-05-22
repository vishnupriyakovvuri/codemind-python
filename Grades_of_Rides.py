m,n,o=map(int,input().split())
if m>50 and n>60 and o>100:
    print('10')
elif m>50 and n>60 and o<100: 
    print('9')
elif m<50 and n>60 and o>100:
    print('8')
elif m>50 and n<60 and o>100:
    print('7')
elif m>50 or n>60 or o>100:
    print('6')
else:
    print('5')