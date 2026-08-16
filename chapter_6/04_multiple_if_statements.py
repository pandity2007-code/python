# multiple if statements
age = int(input("enter the age :"))

if( age%2==0):
    print("age is even number")
if( age >= 18):
    print("you are eligible to vote")
    print("you can vote in the elections")

if(age<0 or age==0):
    print("you have entered an invalid age")
    print("please enter a valid age")

else: 
    print("invalid")