class employee:
    def __init__(self):
        print("contractor of employee")
    a=1
class programmer(employee):
    def __init__(self):
            super().__init__(self)   #self method
            print("contractor of programmer")

            
    b=2
class manager(programmer):
    c=3
o=employee()
#print(o.a) #print the a attributes
#print(o.b )#show an error because b is not the attribute of employee
o=programmer()
# here b is attribute of programmer
print(o.a,o.b)
# o=manager()
# print(o.a,o.b,o.c)