#class with methods
class Circle():
    pi=3.14
    
    #if not provide radius default will be 1
    def __init__(self,radius=1):
        self.radius=radius
    
    # self states method of that class
    #Area and set radius fun should be called not like init function
    def area(self):
        return self.radius*self.radius*Circle.pi

    def set_radius(self,new_r):
        self.radius=new_r

#mycircle=Circle() 
# default 1 print
mycircle=Circle(2)
mycircle.set_radius(2300)
print(mycircle.radius)


print(mycircle.area())
# func lai double