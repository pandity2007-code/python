num=123
reverse=0

while num>0:
    digit=num%10 #
    reverse = reverse * 10 + digit
    num=num//10
print(reverse)    

'''
num%10=123%10 =3
3 = revese
123//10=12
12%10 =2
32
12//10 =1



'''
