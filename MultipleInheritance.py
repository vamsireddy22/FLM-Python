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
    

class B:
    def __init__(self,d,e,f):
        print("Class B Constructor")
        # self.a = a
        # self.b = b
        # self.c = c
        self.d = d
        self.e = e
        self.f = f
        print("Exiting Class B")
    
    def printB(self):
        # print(self.a)
        # print(self.b)
        # print(self.c)
        print(self.d)
        print(self.e)
        print(self.f)


class C(B,A):
    def __init__(self,a,b,c,d,e,f,g,h,i):
        print("Class C Constructor")
        A.__init__(self,a,b,c)
        B.__init__(self,d,e,f)
        self.g = g
        self.h = h
        self.i = i
        print("Exiting Class C")
    
    def printC(self):

        # while using super() ytou don't need to pass self as  default arguement
        A.PrintA(self)
        B.printB(self)
        #super().printA()
        print(self.g)
        print(self.h)
        print(self.i)


objC = C("vamsi","reddy","sai","sumanth","Tejaswini","Soujanya","Supriya","sathish","Roja")
objC.printC()

        
