# sum of n natural numbers using recursion

n = int(input("enter the number:"))

def sum(n):
    if n==1 :  # base condition to avoid the infinite loop
        return 1
    

    return sum(n-1)+n
print(f"sum = {sum(n)}")