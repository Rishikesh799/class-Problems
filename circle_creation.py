class Circle:
    def __init__(self,a,b,r):
        self.a=a
        self.b=b
        self.r=r
    def area(self):
        from math import pi
        print("Area of circle is :",pi*self.r**2)
    def perimeter(self):
        from math import pi
        print("Perimeter of circle is:",2*pi*self.r)
    def cir(self,x,y):
        return (x-self.a)**2+(y-self.b)**2-self.r**2

    def testbelongs(self,x,y):
        if (self.cir(x,y))==0:
            print("rhe point belongs to the circle")
        else:
            print("Points are not belongs to the circle")

c=Circle(2,3,2)
c.area()
c.perimeter()
c.testbelongs(1,2)
