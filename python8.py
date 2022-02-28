#function as argument
#passing function and calling that function inside other func here hello called inside other func
def hello():
    return "Hi saugat"

def other(func):
    print("hey")
    print(func())

other(hello)
