class Person:

    def __init__(self, name):
        self.name = name

class Bike:

    def __init__(self,speeds,owner):
        self.speed = speeds
        self.owner = owner
        self.color = "grey"
    def set_color(self,new_color):
        self.color = new_color

sam = Person("Sam")
bike = Bike(100, sam)

print (bike.owner.name)
