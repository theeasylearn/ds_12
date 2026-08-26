# Hierarchical inheritance 
class MyMath:
    def getPi(self):
        pi = 22/7 #local variable
        return pi 
    def getSquare(self,number):
        square = number * number
        return square

#Circle extends MyMath (derived)
class Circle(MyMath):
    def __init__(self,radius):
        self.radius = radius
    def getArea(self):
        #pi * radius * radius to calculate area of circle 
        area = super().getPi() * super().getSquare(self.radius)
        return area 

class Sphere(Circle):
    def __init__(self,radius):
        super().__init__(radius) 
    #method overidding
    def getArea(self):
        area = super().getArea()
        area = 4 * area
        return area 
class Square(MyMath):
    def __init__(self,size):
        self.size = size 
    def getArea(self):
        return super().getSquare(self.size)

radius = int(input("Enter radius"))
s1 = Sphere(radius)
print("Area of sphere ",round(s1.getArea(),2))


