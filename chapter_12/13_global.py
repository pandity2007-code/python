# global keyword

a=11
def fun():
    global a
    a=23
    print(a)
fun()
print(a)