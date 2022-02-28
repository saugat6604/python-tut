#function lowercase
#class Uppercase
# class Sample():
#     pass

# x=Sample()
# print(type(x))
#<class '__main__.Sample'>

class Dog():
    #class obj attribute
    hello=5
    #init method for initialization
    #init called automatically after obj being reated
    #self tells this method refers to itself ie actual class dog
    #add more attribute such as breed
    #now init method req breed as argument from below obj otherwise error
    def __init__(self, breed,name):
        self.breed=breed
        self.name=name
    
#mydog=Dog(breed="puppy",name="rocky")
mydog=Dog(breed="puppy",name="rocky")
print(mydog.hello)

#bredd puppy sent at initialization
print(mydog.breed)
mydog1=Dog(breed="honey",name="lucky")

print()

#breed is attribute not func so no closed brack