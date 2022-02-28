#returning function
#returning entire function not just only string
def hello(name="saugat"):
    print("the hello func run")
    def greet():
        print ("Hello")
    def welcome():
        print("welcome everyone")

    if name=="saugat":
        return greet
    else:
        return welcome

x=hello()
print(x())