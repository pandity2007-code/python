# celsius into fahrenhiet

# formula = c/5 = f-32/9
#c= 5*(f-32/9)
#f= (c/5)*5-32

c = int(input("enter the temp in celcius:"))

def temp(c):
    return (c/5)*5-32
print(f"celcius in fahrenhiet : {temp(c)}")