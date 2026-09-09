def calculator(a,b,operation):
    match operation:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            return a/b
        case _:
            return "invalid"
a=int(input("enter the number a :"))        
b=int(input("enter the number b :"))       
op=input("enter the operation +,-,*,/ :")

print(calculator(a,b,op))
 