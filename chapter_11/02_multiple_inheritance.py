class employee:
    name='yash'
    company="microsoft"
    def show(self):
        

        print(f"my name is {self.name} and company name is {self.company}")

class coder:
    company="microsoft tech"
    language="python"
    def showlanguage(self):
        print(f"i am best in {self.language}")

class programmer(employee,coder):
    def showself(self):
        print("my name is {self.name }and company is {self.company}")

a=employee()

b=programmer()
a.show()
b.showlanguage()
b.showself()    
                      