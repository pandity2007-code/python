class twovector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"vector is {self.i}i + {self.j}j")    

class threevector(twovector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k=k
    def show(self):
        print(f"vector is {self.i}i + {self.j}j + {self.k}k")

            
a=twovector(2,4)
b=threevector(2,4,5)       
a.show()
b.show()
        