#sum a list with 5 number

number = [0]

n1 = int(input("enter number 1st :"))
number.append(n1)
n2 = int(input("enter number 2nd :"))
number.append(n2)
n3 = int(input("enter number 3rd :"))
number.append(n3)
n4 = int(input("enter number 4th :"))
number.append(n4)
n5 = int(input("enter number 5th :"))
number.append(n5)

print("sum is :",sum(number))