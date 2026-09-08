class animals:
    pass
class pets(animals):
    pass
class dogs(pets):
    @staticmethod
    def bark():
        print("bow bow")

d=dogs()
d.bark()        