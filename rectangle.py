"""
QQQ==Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
     Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
     Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
     Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped.

class Rect:
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        return self.l*self.w

    def perimeter(self):
        return 2*(self.l+self.w)

    def display(self):
        print("Perimeter of reactangle :",self.perimeter(),"m")
        print("Area of reactangle :",self.area(),"m2")
class Parallelpipede(Rect):
    def __init__(self,l,w,h):
        Rect.__init__(self,l,w)
        self.h=h
    def volume(self):
        print("Volume of reactangle :",self.h*self.w*self.l,"m3")
class Square:
    def __init__(self,s):
        self.s=s
    def area(self):
        print("Area of square :",self.s*self.s,"m2")


r = Parallelpipede(11,22,33)
r.display()
r.volume()
s=Square(50)
s.area()


-----------------------
------

















