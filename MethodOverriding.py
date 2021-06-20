'''
    Overriding means accessing the properties and functionalities 
    of base class by using the derived class. 

'''

class Person:

    def printme(self,name,age):
        print(name)
        print(age)
    
class Employee(Person):

    def display(self,name,age,address):
        # Person.printme(self,name,age)
        super().printme(name,age)
        print(name)
        print(age)
        print(address)

emp = Employee() # Default Constructor
emp.display("Vamsi",21,"TPT")
# emp.printme("Vamsi",21)
