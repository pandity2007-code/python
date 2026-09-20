correct_password= "12345"

while True:
    password=input("enter the password:")

    if password==correct_password:
        print("password is correct access granted:")
        break
    else:
        print("password is incorrect")