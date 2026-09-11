# print elements which are divisible by 5

l=[12,15,55,20,115]
def divisble(n):
    if n%5==0:
        return True
    return False
a=list(filter(divisble,l))
print(a)