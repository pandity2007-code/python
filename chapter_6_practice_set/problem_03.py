c1 = "make a lot of money"
c2 = "click here"
c3 = "buy now "
c4 = "subscribe this"


message = input("enter thr message:")
if(c1 in message or c2 in message or c3 in message or c4 in message):
    print("this is spam comment")
else:
    print("there is no spam comment")    
print("Thankyou ")    