# Activity 2: Polymorphism Challenge
class Car:
    def move(self):
        return "Driving"

class Plane:
    def move(self):
        return "Flying"

class Boat:
    def move(self):
        return "Sailing"

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
