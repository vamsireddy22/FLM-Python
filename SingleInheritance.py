''' 
    Properties of Parent:
        Name,age,address
    Properties of student:
        Fname, name, age, Fage, Address, Study, StudPhno, College
'''

class Father:
    def __init__(self, Fname, Fage, Address):
        self.Fname = Fname
        self.Fage = Fage
        self.Address = Address
        print("Object Created at Father Class")

    def PrintFatherDetails(self):
        print(self.Fname,self.Fage,self.Address)
        return


# Inheriting the parent class into Student class
class Student(Father):
    def __init__(self, Name, age, Address,Study, Studphno,College,Fname,Fage):
        super().__init__(Fname, Fage, Address)
        self.Name = Name
        self.age = age
        self.Study = Study
        self.Studphno = Studphno
        self.College = College
        print("Object created at Student class")
    
    def PrintStudentDetails(self):
        print(self.Name,self.age,self.Study,self.College,self.Studphno)
        super().PrintFatherDetails()
        return



print("Creating S1")
s1 = Student("Vamsi",21,"TPT","CSE",1241334,"SVU","Vamsi-Dad",45)

print("Creating S2")
s2 = Student("Sai",23,"KRNL","ECE",46464646,"SVU","Sai-Dad",45)

# Printing the student details

print("Printing the s1")
s1.PrintStudentDetails()
#s1.PrintFatherDetails()


print("printing the s2")
s2.PrintStudentDetails()
#s2.PrintFatherDetails()








