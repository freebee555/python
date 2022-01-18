from lib2to3.pgen2.token import LBRACE


a='1234'
b='98934'

la=len(a)
lb=len(b)

if la>lb:
    b='0'*(la-lb)+b
    m=la
else:
    a='0'*(lb-la)+a
    m=la

na=[int(a[i]) for i in range(m)]
nb=[int(b[i]) for i in range(m)]
print(na,nb)
