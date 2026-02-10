
class Student:
    # attributes
    name = "Jester"
    age = 23
    gender = "Female"
    course = "MIT"

    #Behavior/functions
    def study(self):
        print("Student is studying")

student1 = Student()
student1.study()
print(student1.name)