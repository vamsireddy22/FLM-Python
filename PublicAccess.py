class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name:", self.name)
        print("Age:",self.age)

class Employee(Person):
    def __init__(self, name, age,address):
        super().__init__(name, age)
        self.address = address
    
    def printDetails(self):
        print("Printing in employee class")
        print("Name:", self.name)
        print("Age:",self.age)
        print("Address: ",self.address)

objectEmployee = Employee("Vamsi",21,"TPT")
objectEmployee.printDetails()
print("Printing in main class")
print("Name : ",objectEmployee.name)
print("Age:",objectEmployee.age)
print("Address: ",objectEmployee.address)