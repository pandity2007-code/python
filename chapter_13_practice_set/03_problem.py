from functools import reduce

l=[1,2,3,4,5]
def mul(a,b):
    return a*b
print(reduce(mul,l))