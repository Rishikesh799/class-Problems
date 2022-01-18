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
class Computation:
    def fact(self,x):
        s=1
        for i in range(1,x+1):
            s=s*i
        print("Factoraial of number is :",s)

    def sum(self,n):
        k=0
        for i in range(1,n+1):
            k=k+i
        print("The total sum is n integers:",k)

    def testprime(self,y):
        co=0
        if y>1:
            for i in range(1,y+1):
                if y%i==0:
                    co=co+1
            if co == 2:
                return True
            else:
                return False

    def testcoprims(self,l,m):

        if (self.testprime(l))and (self.testprime(m)):
            print("co prime")

        else:
            print("no")

    def tablemult(self,r):
        for j in range(1,r+1):
            for i in range(1,11):
                print(j,"*",i,"=",i*j)
            print()


    def listdiv(self,j):
        Ldiv=[]
        for i in range(1,j+1):
            if j%i==0:
                Ldiv.append(i)
        print(Ldiv)
        self.Ldiv=Ldiv


    def listdivprime(self,z):
        a=[]
        for o in self.Ldiv:
            if self.testprime(o)==True:
                a.append(o)
        print("divisors are prime are:",a)

c = Computation()
print(c.testprime(18))
c.sum(18)
c.fact(18)
c.testcoprims(11,13)
c.tablemult(6)
c.listdiv(18)
c.listdivprime(18)
"""
















