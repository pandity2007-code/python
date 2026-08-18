n = int(input("enter the number:"))

for i in range(2,n):
    if(n%i==0):  # it checks that  num is divided by any number between 2 and n  
        print("the number is not prime")
        break
else:
    print("the number is prime")        