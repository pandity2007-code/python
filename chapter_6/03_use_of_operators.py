# using operators: relational and logical operators


age = int(input("enter the age :"))

if( age >= 18):  # relational operator
    print("you are eligible to vote")
    print("you can vote in the elections")

elif(age<0and age==0):  # logical operator
    print("you have entered an invalid age")
    print("please enter a valid age")

elif(age<0 or age==0):   
    print("you have entered an invalid age")
    print("please enter a valid age")