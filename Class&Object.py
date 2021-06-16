# House Program 

# create a class 

class House:
    
    # Properties : Hname, Hno, Area(Sq.ft), Address, Facing
    # Constructor which is used to create the object. 
    # Constructor will never return a value
    # While creating the objects it initializes the values to class properties. 

    def __init__(self, Hname, Hno, Area, Address,  Facing): # 2 underscore inti 2 underscores
        
        # Self is kindof pointer which helps to map the values to its current objects
        # Instances Variables
        print("Object is being created")
        self.Hname = Hname
        self.Hno = Hno
        self.Area = Area
        self.Address = Address
        self.Facing = Facing
        print("Object is created")

    def HouseDetails(self): 

        # If a function inside a class then we need to call it has a "Method".
        # A method in a class represents as a functionality of class
        print(self.Hname)
        print(self.Hno)
        print(self.Address)
        print(self.Area)
        print(self.Facing)


        

h1 = House("Vamsi House",2031, 1000, "TPT", "North") # Object craetion
h2 = House("Padma House",2032, 1500, "TPT", "West")
h3 = House("Sai House",2033, 1100, "TPT", "East")


h2.HouseDetails()
h3.HouseDetails()
h1.HouseDetails()

# Function call - factorial(n)