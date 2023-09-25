# inheritance
class Car :
    def __init__(self, name, id) :
        self.name = name
        self.id = id
    def printer(self) :
        print("Car Name :", self.name," :: ID",self.id)

class Audi(Car) :
    def __init__(self, id, name, engine, nbPortes) :
        super().__init__(name, id)
        self.engine = engine
        self.nbPortes = nbPortes
    def carType(self) :
        super().printer()
        print("NB Portes :", self.name,":: Engine :", self.engine)

myCar = Audi(0, "Khaled", "AMG", 2)
myCar.carType()



# Class attributes
class Person :
    nbOfPersons = 0
    def __init__(self, name) :
        self.name = name
        Person.addPerson()

    @classmethod
    def printer(cls) :
        print(cls.nbOfPersons)

    @classmethod
    def addPerson(cls) :
        cls.nbOfPersons+=1
class imployee(Person) :
    def __init__(self, name):
        super().__init__(name)
        
    
p1 = imployee("Person1")
p2 = imployee("Person2")
p1.printer()