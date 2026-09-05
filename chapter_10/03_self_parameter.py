class Employee:
    
    age=18
    language="py"
    def getinfo(self):
        print(f"the language is {self.language} and the age is {self.age}")


harry=Employee()
harry.language="c"

harry.getinfo()