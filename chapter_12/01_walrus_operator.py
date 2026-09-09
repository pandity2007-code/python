if name:=input("enter the name:"): # here walrus does two things takes input and store it in name
    print("hello ",name)

# with while loop

while(n:=int(input("enter the number :")))>0:

    print("number :",n)
    break


if(guess:=int(input("guess the number :")))>n:
    print("lower number please")