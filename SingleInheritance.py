# Single Inheritance

class Person:
    def __init__(self,name,mobile,address):
        print("I am inside the person contructor")
        self.name = name
        self.mobile = mobile
        self.address = address
    
    def printDetailsOfPerson(self):
        print("I am inisde the person class and printing the person details")
        print(self.name)
        print(self.mobile)
        print(self.address)

class Employee(Person):
    def __init__(self,name,mobile,address,eid,company,sal):
        print("I am in Employee Constructor")
        Person.__init__(self,name,mobile,address)
        self.eid = eid
        self.company = company
        self.sal = sal
        print("I am exiting the Employee Constructor")
    
    def PrintEmployeeDetails(self):
        print("I am printing details of Employee")
        print(self.name)
        print(self.mobile)
        print(self.address)
        print(self.eid)
        print(self.company)
        print(self.sal)
        

    

emp = Employee("Vamsi",124324,"TPT","e007441","Google",100000)
#emp.PrintEmployeeDetails()
emp.printDetailsOfPerson()

# person1 = Person("Vamsi",12342325,"TPT")
# person1.printDetailsOfPerson()


