class Bird:
    def Intro(self):
        print("I am Bird")
    def fly(self):
        print("Every bird can fly")

class parrot(Bird):
    def fly(self):
        print("A parrot can fly upto some hieght")

class Eagle(Bird):
    def fly(self):
        print("I am eagle I can fly morethan anyother bird")


objBird = Bird()
objParrot = parrot()
objEagle = Eagle()

for obj in (objBird,objEagle,objParrot):
    obj.Intro()
    obj.fly()