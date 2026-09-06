
class Employee:
    
    age=18
    language="py"
    @staticmethod
    def getinfo():
        print("good morning")


harry=Employee()
harry.language="c"
print(harry.age,harry.language)

harry.getinfo()