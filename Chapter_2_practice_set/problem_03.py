# check the type  of  variable assigned using input type()function.

a = input("enter the number a ")

b= type(a) 
print("type of a is :", b) # it returns every time <class 'str'> type because the value of a is stored as str


a = int(input("enter the number a:"))
b= type(a) 
print("type of a is :", b)