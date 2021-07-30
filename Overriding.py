class House:
    def methodA(self):
        print("I am in House MethodA")
    
class Person:
    def methodA(self):
        print("I am in Person MehtodA")
    
objHouse = House()
objPerson = Person()

for obj in (objHouse,objPerson):
    obj.methodA()

# Why this is runtime
