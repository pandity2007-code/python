a=int(input("enter the number:"))
b=int(input("enter the number:"))
if(b==0):
    raise ZeroDivisionError("our program is not to meant to divided by 0")
else:
    print(f"divide of a/b {a/b}")