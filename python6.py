#function inside function

def hello(name="saugat"):
    print("the hello func run")
    def greet():
        print ("Hello")
    def welcome():
        print("welcome everyone")

    print(greet())
    print(welcome())
hello()

#welcome()
#canot call welcome from outside here because it is inside scope of hello function
