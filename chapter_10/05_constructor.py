class Employee:

    c="c"
    age=18
    language="py"

    def __init__(self,name,age,language):
        self.age= age
        self.language=language
        self.name=name
        print("i am creating a object")
    @staticmethod
    def getinfo():
        print("good morning")


harry=Employee("yash",18,"ruby")

print(harry.name,harry.age,harry.language)

harry.getinfo()