try:
    a=int(input("enter the number:"))
    print(a)
except ValueError:
    print("Please enter a valid integer.")
else:                       # this is executed only if the try was succesful
    print("i am inside the else")