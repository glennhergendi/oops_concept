class person:
    age = 12
    def __init__(self, name):
        self.name = name
    def printHi(self):
        print("Hi, name is", self.name)

class Student(person):
    def study(self):
        print("i am studying")
student1 = Student('Halip')
student2 = Student('Fitraka')
student3 = Student('Glenn')

student1.printHi()
print("my age is", student1.age, "years old")
student1.study()

student2.printHi()
print("my age is", student2.age, "years old")
student2.study()

student3.printHi()
print("my age is", student3.age, "years old")
student3.study()
