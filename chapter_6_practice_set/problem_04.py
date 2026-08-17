#check username contain less than or more than 10 charcters

username = input("enter your username :")

if(len(username)<10):
    print("username contain less than 10 character")
elif(len(username)>10):
    print(" username contain more than 10 charcters")
elif(len(username)==10):
    print("usename contains equal to 10 characters")        
else:
    print("Thankyou")    