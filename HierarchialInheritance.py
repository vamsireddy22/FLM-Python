class A:
    def __init__(self):
        print("Objects created at A")
    
    def PrintingA(self):
        print("Printing at A")

class B(A):
    def __init__(self):
        print("Objects created at B")
    
    def PrintingB(self):
        print("Printing at B")

class C(A):
    def __init__(self):
        print("Objects created at C")
    
    def PrintingC(self):
        C.PrintingA(self)
        print("Printing at C")

class D(A):
    def __init__(self):
        print("Objects created at D")
    
    def PrintingD(self):
        D.PrintingA(self)
        print("Printing at D")

objectD = D()
objectC = C()
objectC.PrintingC()
objectD.PrintingD()

