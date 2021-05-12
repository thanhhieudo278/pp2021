
class Student:

    def __init__(self, id, name, DoB ):
        self.id = id
        self.name = name
        self.DoB = DoB


    def print(self):
        print("ID of student :", self.id)
        print("Name of student:", self.name)
        print("DoB of student:", self.DoB)