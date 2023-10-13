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

"""myCar = Audi(0, "Khaled", "AMG", 2)
myCar.carType()"""


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
        
class Persons :
    nbperson = 0
    listName = []
    @classmethod
    def __init__(cls) :
        cls.listName = []

    def addPerson(self, name, id = -1) :
        self.name = name

        self.id = Persons.nbperson if (id == -1) else id

        Persons.listName.append((self.id, self.name.title()))
        Persons.addpersonCount()

    @classmethod
    def printerName(cls, id) :

        while (id >= len(cls.listName) or id < 0) :
            id = int(input("Please, Give an id number within (0 - {}) : ".format(len(cls.listName) - 1)))
        print("{} : \"{}\"".format(cls.listName[id][0], cls.listName[id][1]))
        
    
    @classmethod
    def numbersCount(cls) :
        print("There {} person in your sociaty".format("are {}".format(cls.nbperson) if Persons.nbperson >1 else "is a"))
    
    @classmethod
    def addpersonCount(cls) :
        cls.nbperson+=1

    def printAllNames(self) :
        print("\nAll The Sociaty names :")
        for id, _ in Persons.listName :
            self.printerName(id)
        print()

persons = Persons()
persons.addPerson("Name LastName")
persons.addPerson("Name1 LastName1")
persons.printerName(0)
persons.printAllNames()

class Math :
    # We can't change in a static method
    @staticmethod
    def mod(number, x) :
        return number % x
    
    @staticmethod
    def floatDiv(number, x) :
        return number / x
print(Math.floatDiv(5,2))

"""
p1 = imployee("Person1")
p2 = imployee("Person2")
p1.printer()"""
