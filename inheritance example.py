class shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    def area(self):
        print("i am area method of shape class")



class Triangle(shape):
    def area(self):
        area  = 0.5 * self.dim1 * self.dim2
        print("Area of triangle: ",area)



class Rectangle(shape):
    def area(self):
        area  = self.dim1 * self.dim2
        print("Area of Rectangle: ",area)

t1 = Triangle(20,30)
t1.area()
r1 = Rectangle(10,10)
r1.area()