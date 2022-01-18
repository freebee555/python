
a='76587691123412341234698726349587263459826'
b='87856763813294871328946192386419372641234'

oa=a
ob=b

la=len(a)
lb=len(b)
if len(a)>len(b):
    b=('0'*(la-lb))+b
    m=la
elif la<=lb:
    a=('0'*(lb-la))+a
    m=lb

c=[0 for i in range(m+1)]

i=m
while i>0:
    c[i]=int(a[i-1])+int(b[i-1])
    i=i-1

i=m
while i>0:
    n1=c[i]
    n2=int(n1/10)
    n3=n1%10
    c[i]=n3
    c[i-1]=c[i-1]+n2
    i=i-1

output=''
for sc in c:
    output=output+str(sc)


print(oa+' + '+ob+' = '+output[output[0]=='0':m+1])
