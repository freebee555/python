def output(*numbers):
    nn=''
    for sn in numbers:
        nn=nn+str(sn)
    i=len(nn)
    while i>=0:
        if nn[0]=='0':
            nn=nn[1:len(nn)]
            i=i-1
        else:
            break
    return nn

a='23456563456541334'
b='98847'

la=len(a)
lb=len(b)
oa=a
ob=b

if la>lb:
    b='0'*(la-lb)+b
    m=la
else:
    a='0'*(lb-la)+a
    m=lb

na=[int(a[i]) for i in range(m)]
nb=[int(b[i]) for i in range(m)]

##################ADD##########################
c_add=[0 for i in range(m+1)]

for i in range(m):
    c_add[i+1]=na[i]+nb[i]


i=m
while i>=0:
    n1=c_add[i]
    n2=int(n1/10)
    c_add[i]=n1%10
    c_add[i-1]=c_add[i-1]+n2
    i=i-1

print(oa+' + '+ob+' = '+output(*c_add))

################Multiply#################
c_mp=[0 for i in range(m*2)]

i=m-1
while i>=0:
    j=m-1
    while j>=0:
        n1=na[j]*nb[i]
        c_mp[i+j+1]=n1+c_mp[i+j+1]
        j=j-1
    i=i-1

i=m*2-1
while i>=0:
    n1=c_mp[i]
    n2=int(c_mp[i]/10)
    c_mp[i]=n1%10
    c_mp[i-1]=c_mp[i-1]+n2
    i=i-1

op=output(*c_mp)
print(oa+' * '+ob+' = '+op[op[0]=='0':len(op)])



