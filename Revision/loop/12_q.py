# factorial using for loop

n=int(input("enter the number :"))

product=1

for i in range(1,n+1):
    product*=i
print(product)