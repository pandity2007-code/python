class employee:
    a=1
class programmer(employee):
    b=2
class manager(programmer):
    c=3
o=employee()
print(o.a) #print the a attributes
#print(o.b )#show an error because b is not the attribute of employee
o=programmer()
# here b is attribute of programmer
print(o.a,o.b)
o=manager()
print(o.a,o.b,o.c)