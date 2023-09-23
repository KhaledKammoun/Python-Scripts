class car :
    def __init__(self, name) :
        self.name = name
    
    def showCar(self) :
        print("Name :",self.name)
        
class audi(car) :
    def __init__(self, name, maxSpeed) :
        super().__init__(name) # calling methods or constructors from the parent class
        self.maxSpeed = maxSpeed

    def showMaxSpeed(self) :
        print("Max Speed :",self.maxSpeed)
        super().showCar()
car1 = audi("Audi A5", 5)
car1.showMaxSpeed()
