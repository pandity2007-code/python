#printing the 3rd ,5th,7th element of a list using list emumerate function


list1=[1,4,5,76,3,4,24,67,89,97,5,24,55]

for index,item in enumerate(list1):
    if index==2 or index==6 or index==8:
        print(item)