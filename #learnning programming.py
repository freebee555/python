from tkinter.font import names


names=['nancy','good','albert','ctrip','sohu']

print(names)

for name in names:
    print(name.upper())

sum=0
for n in range(101):
    sum=sum+n
    print('sum%d=%d'%(n,sum))

L = {'Bart':33, 'Lisa':22, 'Adam':55,'Bart':66}
for n in L:
    print('hello '+n)

print(L['Bart'])
print(L.get('Lisa',-1))

s = set([1, 2, 3])
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1|s2)

s3=['招招','中国工商银行','中国农业银行','中国银行','中国建设银行','交通银行','中国民生银行','招商银行','兴业银行','广发银行']
s3.sort()
print(s3)

s4=['a','y','f','h','g']
s4.sort()
print(s4)

print(oct(1200))



def my(x):
    if x%2==1:
        return 'odds'
    else:
        return 'even'

#n=int(input('n='))
#print(my(n))

m=40
n=m
while n>1:
    print(' '*n+'*'*((m+1-n)*2-1))
    n=n-1


import math

def move(x, y, step, angle=1):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi )
print(x,y)

def qr(a,b,c):
    tmp=math.sqrt(b*b-4*a*c)
    n1=(-b+tmp)/(2*a)
    n2=(-b-tmp)/(2*a)
    return n1,n2

a=1
b=3
c=-4
print(qr(a,b,c))