# star patttern

def pattern(n):
   
    if n==0:
        return  
    print("*"*n)
   
    pattern(n-1)
print(pattern(5))    