# factorial of n number using loop

n = int(input("enter the number:"))
product=1
for i in range (1,n+1):
    product*=i
    i+=1

print(f"factorial of {n} is = {product}")