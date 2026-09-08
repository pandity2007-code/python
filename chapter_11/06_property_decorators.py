class programmer:
    a=45
    @classmethod
    def show(self):


        print(f"value of a is {self.a}")
    @property
    def name(self):
        return {self.fname,self.lname}
    @name.setter

    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
e=programmer()
e.name="yash saraswat"
print(e.fname,e.lname)
e.show()
     