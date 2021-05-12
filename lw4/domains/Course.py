class Course:

    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit


    def print(self):
        print("ID of Course:", self.id)
        print("Name of Course:", self.name)
        print("Name of credit:", self.credit)