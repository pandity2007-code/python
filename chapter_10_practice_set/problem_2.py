class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"square of {self.n} : {self.n*self.n}") 
    def cube(self):
        print(f"cube of {self.n}:{self.n**3}")       
    def cuberoot(self):
        print(f"cube of {self.n}:{self.n**1/2}")       

a=calculator(4) 
a.square()       
a.cube()
a.cuberoot()