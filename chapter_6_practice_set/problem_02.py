# student is paased or falied if he scored total 40% in three subjects and minimum 33% in each subject

marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

total_percentage = (100*(marks1 + marks2 + marks3) / 300)

if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("The student is passed")
else:
    print("The student is failed")
    