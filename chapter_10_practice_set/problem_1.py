class programmer:
    company="microsoft"   #class attribute
   
    def __init__(self,name,salary,pin):    #dunder method which is automatically called
        self.name=name
        self.salary=salary
        self.pin=pin

p=programmer("yash",100000,202140)  
print(p.name,p.salary,p.pin,p.company)        