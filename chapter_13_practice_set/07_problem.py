from functools import reduce
l=[9784,334,34543,5678765,5432,23,4]

def greater(a,b):
    if a>b:
      return a
    return b
print(reduce(greater,l))