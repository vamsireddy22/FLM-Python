class Person:
    # Self points to current object
    def __init__(self, name, age, address):
        print("I am in person constructor")
        self.name = name
        self.age = age
        self.address = address
    
    def PrintPersonDetails(self):
        print("I am in Person class Printing")
        print(self.name)
        print(self.age)
        print(self.address)
    
class Employee(Person): # Inheriting Person class
    def __init__(self,name,eid,age,address):
        print("I am in Employee class constructor")
        super().__init__(name,age,address)
        self.eid = eid
    
    def PrintEmployeeDetails(self):
        print("I am in employee class print details")
        super().PrintPersonDetails()
        print(self.eid)

class Manager(Employee):
    def __init__(self,name,age,eid,exp,address):
        print("I am in Manager constructor")
        self.exp = exp
        super().__init__(name,eid,age,address)

    def PrintManagerDetails(self):
        print("I am in Manager class printing")
        super().PrintEmployeeDetails()
        print(self.exp)




mang1 = Manager("Vamsi",45,12345,15,"TPT")

# emp = Employee("Vamsi",1234,21,"TPT")
# #emp1 = Employee("Sai",123456,23,"KRNL")

# p1 = Person("Vamsi",21,"TPT")

print("Printing Manager")
mang1.PrintManagerDetails()

# print("Printing Employee")
# emp.PrintEmployeeDetails()
# print("Printing person")
# p1.PrintPersonDetails()






    







