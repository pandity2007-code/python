class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, other):
        result=vector(self.x+other.x,self.y+other.y,self.z+other.z)   
        return result 
    def __mul__(self, other):
        result= self.x*other.x + self.y*other.y + self.z*other.z
        return result
    def __str__(self):
        return f"{self.x}i,{self.y}j,{self.z}k"

v1=vector(1,2,3)
v2=vector(4,1,3)
v3=vector(1,5,1)
print(v1+v2+v3)
print(v1*v2)