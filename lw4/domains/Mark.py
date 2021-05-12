
class Mark:

    def __init__(self, id_course, id_student, mark):
        self.id_course = id_course
        self.id_student = id_student
        self.mark = mark

    def print(self):
        print("ID of student:", self.id_student)
        print("ID of course:", self.id_course)
        print("mark :", self.mark)