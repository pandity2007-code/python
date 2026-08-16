#if elif else ladder

age = int(input("enter the age :"))

if(
    age >= 18):
    print("you are eligible to vote")
    print("you can vote in the elections")

elif(age < 0):
        print("you have entered an invalid age")
        print("please enter a valid age")

elif(age ==0):
    print("you have entered an invalid age")
    print("please enter a valid age")
     
         
else:
    print("you are not eligible to vote")
    print("you cannot vote in the elections")
    print("you have to wait for", 18 - age, "years to vote")

print("thank you for using this program")