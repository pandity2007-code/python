a = int(input("enter the first number:"))

b = int(input("enter the second  number:"))

c = int(input("enter the third number:"))

def greater(a,b,c):
    if(a>b and a>c):
        print("A is the greatest number")
    elif(b>a and b>c):
        print("B is the greatest number")
    elif(c>a and c>b):
        print('C is the greatest number')
    if a==b or b==a:
        print("a and b are greatest & equal to each other")
        if a==c or c==a:
            print("a and c are equal & to each other")  
    if b==c or c==b:
        print('b and c are equal & to each other')              
greater(a,b,c)        