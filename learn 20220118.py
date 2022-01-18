def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

a=[i for i in range(1,100)]
print(a)
print(calc(*a))