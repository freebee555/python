def output(*numbers):
    nn=''
    for sn in numbers:
        nn=nn+str(sn)
    return nn[nn[0]=='0':len(nn)]

a='13'
b='138456877475847'

la=len(a)
lb=len(b)

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

print(a+' + '+b+' = '+output(*c_add))

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
print(a+' * '+b+' = '+op[op[0]=='0':len(op)])



