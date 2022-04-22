for val in "bangla":
    if val == "l":
        break
    print(val)

print("the end")



for val in "bangla":
    if val == "g":
        continue
    print(val)

print("the end")

class Car:
    def __init__(self,color,brand):
        self.color = color
        self.brand = brand
#car object
car1 = Car("red", "bmw")
car2 = Car("blue", "toyota")
car3 = Car("black", "audi")

#check results
print("This car\'s color is " + str(car1.color) + " and brand name is " + car1.brand)
print("This car\'s color is " + str(car2.color) + " and brand name is " + car2.brand)
print("This car\'s color is " + str(car3.color) + " and brand name is " + car3.brand)