
class A:
    def __init__(self):
        print("Objects created at A")
    
    def DisplayA(self):
        print("Printing at A",self)
    
class B(A):
    def __init__(self):
        super().__init__()
        print("Objects created at B")
    
    def DisplayB(self):
        print("Printing at B")

class C(B):
    def __init__(self):
        super().__init__()
        print("Object created at C")

    def DisplayC(self):
        A.DisplayA(self)
        B.DisplayB(self)
        # B.DisplayA(self)
        print("Printing at C")

objectc= C()
objectc.DisplayC()
objectA = A()
objectA.DisplayA()