#inheritance and special method
#base class and derive class
#derived class overrides base class

class Animal():

    def __init__(self):
        print("we create animal")

    def whoAmI(self):
        print("Animo")

    def eat(self):
        print('Eating')

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("DOg created")

    def eat(self):
        print("dog override animal eat")

myan=Animal()
myan.whoAmI()
myan.eat()

#caling animal init
#derived class dog calling func from base class
dog=Dog()
dog.eat()
dog.whoAmI()