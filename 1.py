
a='1234'
b='98934'

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

print(a+' + '+b+' = '+str(c_add))

################Multiply#################
c_mp=[0 for i in range(m*2)]
print(c_mp)



