'''
    In python the method which defined atlast in class with same method name 
    will be called by default. 

'''

class Person:
    
    def printDetails(self,name,age):
        print(name)
        print(age)
    
    def printDetails(self,name,age,address):
        print(name)
        print(age)
        print(address)

personObject = Person()
personObject.printDetails("Vamsi",21,"TPT") # Will print successfully
personObject.printDetails("Vamsi",21) # Will result in error