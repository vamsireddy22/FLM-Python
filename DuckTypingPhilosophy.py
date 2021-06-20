'''

    When every class has same methodNames and properties 
    then we can take the advantage of dynamic nature of python. 

    Without the creating the separate objects 
    we can use sinle object in a function and call every class

'''

class A:
    def display(self):
        print("I am in Class A")

class B:
    def display(self):
        print("I am in Class B")

class C:
    def display(self):
        print("I am in Class C")


def call(obj): # obj = A() # name ="Vamsi"
    obj.display() 


ls = [A(),B(),C()]
for i in ls:
    call(i)



