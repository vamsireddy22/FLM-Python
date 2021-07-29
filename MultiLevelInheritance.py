# MultiLevel Inheritance
class A:
    def __init__(self,a,b,c):
        print("Class A Constructor")
        self.a = a
        self.b = b
        self.c = c
        print("Exiting Class A")

    def PrintA(self):
        print(self.a)
        print(self.b)
        print(self.c)
    

class B(A):
    def __init__(self,a,b,c,d,e,f):
        print("Class B Constructor")
        #A.__init__(self,a,b,c)

        # Super is used to call base class properties and functionalities
        super().__init__(a,b,c)
        self.d = d
        self.e = e
        self.f = f
        print("Exiting Class B")
    
    def printB(self):
        super().PrintA()
        print(self.d)
        print(self.e)
        print(self.f)


class C(B):
    def __init__(self,a,b,c,d,e,f,g,h,i):
        print("Class C Constructor")
        super().__init__(a,b,c,d,e,f)
        self.g = g
        self.h = h
        self.i = i
        print("Exiting Class C")
    
    def printC(self):
        super().printB()
        print(self.g)
        print(self.h)
        print(self.i)


objC = C(10,20,30,40,50,60,70,80,90)
objC.printC()

        
