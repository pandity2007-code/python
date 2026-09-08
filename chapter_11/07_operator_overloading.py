class number:
    def __init__(self,n):
        self.n=n
    def __add__(self, num):         #add method
        return self.n + num.n
a=number(2)
b=number(5)
print(a+b)
    
        