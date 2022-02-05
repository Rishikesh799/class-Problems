#######COMPUTATION PROBLEM###########
#1 - Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
#2 - Create a method called Factorial() which allows to calculate the factorial of an integer.
#    Test the method by instantiating the class.
#3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
#4 - Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
#4 - Create  a method called testPrims() allowing to test if two numbers are prime between them.
#5 - Create a tableMult() method which creates and displays the multiplication table of a given integer.
#    Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
#6 - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv.
#    Create another listDivPrim() method that gets all the prime divisors of a given integer.

"""
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
-----------------------------------------------------------
OUTPUT==False
The total sum is n integers: 171
Factoraial of number is : 6402373705728000
co prime
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20

3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30

4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
4 * 10 = 40

5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
6 * 10 = 60

[1, 2, 3, 6, 9, 18]
divisors are prime are: [2, 3]
"""

