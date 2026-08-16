#if else conditionals
age = int(input("enter the age :"))

if(
    age >= 18):
    print("you are eligible to vote")
    print("you can vote in the elections")
else:
    print("you are not eligible to vote")
    print("you cannot vote in the elections")
    print("you have to wait for", 18 - age, "years to vote")
