'''
    Overriding means accessing the constructor 
    of base class by using the derived class. 

'''

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printMe(self):
        print(self.name)
        print(self.age)
    
class Employee(Person):

    def __init__(self,name,age,address):
        # Person.__init__(self,name,age)
        super().__init__(name,age)
        
    
    def display(self):
        # Person.printme(self,name,age)
        # super().printme(name,age)
        print(self.name)
        print(self.age)
        print(self.address)
        

emp1 = Employee("Vamsi",21,"TPT")
#emp = Employee("Vamsi",21,"TPT") # Default Constructor
#emp.display()
# emp.printme("Vamsi",21)
emp1.printMe()