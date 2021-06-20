'''
    In python the constructor which defined atlast in class will be called by default. 

'''

class Person:
    
    def __init__(self,name,age):
        print("Constructor with 2 parameters called")
        self.name = name
        self.age = age
    
    def __init__(self,name,age,address):
        print("Constructor with 3 parameters called")
        self.name = name
        self.age = age
        self.address = address

# personObject = Person("Vamsi",21,"TPT") # Will print successfully
personObject2 = Person("Vamsi",21) # Will result in error