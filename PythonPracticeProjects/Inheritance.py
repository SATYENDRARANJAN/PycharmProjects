class Car():
    def __init__ (self,name , price ,brand):
        self.name = name
        self.price =price
        self.brand = brand

class Benz(Car):
    def __init__ (self,name, price , brand):
        # Car.__init__(self,name, price,brand)
        super().__init__(name , price , brand )
        self.name = "CV200"



if __name__== "__main__":
    obj = Benz("CV100","65000","BENZ")

    print(obj.name)