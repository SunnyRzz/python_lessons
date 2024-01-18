#Part1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def how_old(self):
        print(f"{self.name} is {self.age} years old")

    def __str__(self):
        return f"{self.name}, {self.age}"

student1=Student("Adam", 18)
student2=Student("John", 21)

student1.how_old()
print(student2)

#Part2
class Student:
    def __init__(self, name, age, _class):
        self.name = name
        self.age = age
        self._class= _class


    def how_old(self):
        print(f"{self.name} is {self.age} years old")

    def average_scores(self, test1, test2, test3):
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        print(f"{self.name}'s score average is: ", round((self.test1 + self.test2 +self.test3)/3))

    def __str__(self):
        return f"{self.name}, {self.age}, {self._class}"
    
student1=Student("Adam", 18, "Junior")
student2=Student("John", 21, "Senior")

student1.average_scores(75,35,50)

print(student2)

#Part3
class Bird:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def info(self):
        print(f"The bird called {self.name} is of {self.breed} breed")

    def __str__(self):
        return f"{self.name}, {self.breed}"

class Owl(Bird):
    def __init__(self,name,breed):
        super().__init__(name,breed)

    def hoot(self):
        print("Hoot! Hoot!")

    def __str__(self):
        return f"{self.name}, {self.breed}"

class Dodo(Bird):
    def __init__(self,name,breed,extinct):
        super().__init__(name,breed)
        self.extinct = extinct

    def details(self):
        print(f"The bird breed {self.breed} is {self.extinct}")

    def deet(self):
        return super().__str__() + f"exitint - {self.extinct}"

pigeon=Bird("Pidgy", "Pigeon")
print(pigeon)

owl=Owl("Owly","Owl")
owl.hoot()
print(owl)

dodo=Dodo("Doddy", "Dodo", "Extinct")
dodo.details()
print(dodo.deet())
print(dodo)
