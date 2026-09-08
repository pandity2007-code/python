class employe:
    salary=2345
    increment=22
    @property
    def salaryafterincrement(self):
        return (self.salary+self.salary*(self.increment/100))
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        
        self.increment=((salary/self.salary)-1)*100




a =employe()
a.salaryafterincrement=2860

print(a.increment,a.salaryafterincrement)