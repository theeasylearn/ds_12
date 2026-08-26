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

class Square(MyMath):
    def __init__(self,size):
        self.size = size 
    def getArea(self):
        return super().getSquare(self.size)

radius = int(input("Enter radius"))
c1 = Circle(radius)
print("Area of circle ",c1.getArea())

area = int(input("Enter size of square"))
s1 = Square(area)
print("Area of Square ",s1.getArea())
    