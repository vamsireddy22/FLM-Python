class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age # 2 underscores
    
    def display(self):
        print("Name:", self.name)
        print("Age:",self.__age)

class Employee(Person):
    def __init__(self, name, age,address):
        super().__init__(name, age)
        self.address = address
    
    def printDetails(self):
        print("Printing in employee class")
        super().display()
        print("Address: ",self.address)

objectEmployee = Employee("Vamsi",21,"TPT")
objectEmployee.printDetails()
print("Printing in main class")
print("Name : ",objectEmployee.name)
#print("Age:",objectEmployee.age)
print("Address: ",objectEmployee.address)


# per = Person("Vamis",21)
# per.display()