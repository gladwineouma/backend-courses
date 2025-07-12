# this is a class
class Pupil:
    name = "Joanita"
    age = 21
    school = "AkiraChix"
    country = "Uganda"


# this is a constructor
class Student:
    school = "AkiraChix"
    def __init__(self, first_name,last_name,age,country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        

    def greet_student(self):
        return f"Hello {self.name}, welcome to {self.school}"

    def initials(self):
        return f" {self.first_name} {self.last_name} "

        