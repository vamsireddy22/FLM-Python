class A:
    def __init__(self,Aa,Ab,Ac):
        self.Aa = Aa
        self.Ab = Ab
        self.Ac = Ac
    
    def PrintA(self):
        print(self.Aa,self.Ab,self.Ac)

class B:
    def __init__(self,Ba,Bb,Bc):
        self.Ba = Ba
        self.Bb = Bb
        self.Bc = Bc

    def PrintB(self):
        print(self.Ba,self.Bb,self.Bc)


class C(A,B):
    def __init__(self,Aa,Ab,Ac,Ba,Bb,Bc,Ca,Cb,Cc):
        A.__init__(self,Aa,Ab,Ac)
        B.__init__(self,Ba,Bb,Bc)
        self.Ca = Ca
        self.Cb = Cb
        self.Cc = Cc

    def PrintC(self):
        A.PrintA(self)
        B.PrintB(self)
        print(self.Ca,self.Cb,self.Cc)

objC = C(1,2,3,4,5,6,7,8,9)
objC.PrintC()


