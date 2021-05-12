import math
import numpy as np

class Student:

    def __init__(self, id, name, DoB ):
        self.id = id
        self.name = name
        self.DoB = DoB


    def print(self):
        print("ID of student :", self.id)
        print("Name of student:", self.name)
        print("DoB of student:", self.DoB)


def Number_of_Student():
    global nos
    nos = int(input("Number of Students: "))
    return nos

def Make_Student_List():
    for i in range(nos):
        Student_List.append(i)

def Student_Information():
    for i in range (nos):
        print("Enter Student Information: ")
        Student_List[i] = Student(int(input("id:")),input("name: "),input("DoB: "))
        Student_id.append(Student_List[i].id)

def Show_Student_Information():
    for i in range (nos):
        print(i+1, " Student Information : ")
        Student_List[i].print()





class Course:

    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit


    def print(self):
        print("ID of Course:", self.id)
        print("Name of Course:", self.name)
        print("Name of credit:", self.credit)

def Number_of_Course():
    global noc
    noc = int(input("Number of Courses: "))
    return noc

def Make_Course_List():
    for i in range(noc):
        Course_List.append(i)

def Course_Information():
    for i in range (nos):
        print("Enter Course Information: ")
        Course_List[i] = Course(int(input("id:")),input("name: "),int(input("credits of course:")))
        Course_id.append(Course_List[i].id)

def Show_Course_Information():
    for i in range (nos):
        print( i+1 ," Course Information : ")
        Course_List[i].print()


class Mark:

    def __init__(self, id_course, id_student, mark):
        self.id_course = id_course
        self.id_student = id_student
        self.mark = mark

    def print(self):
        print("ID of student:", self.id_student)
        print("ID of course:", self.id_course)
        print("mark :", self.mark)


def Number_of_Mark():
    global nom
    nom = int(input("Number of Marks: "))
    return nom
def Make_Mark_List():
    for i in range(nom):
        Mark_List.append(i)
def Input_Mark():
    global Input_Course_id, mark
    for i in range(nom):
        Input_Student_id = int(input("Enter StudentID to input Mark: "))
        if Input_Student_id in Student_id:
            Input_Course_id = int(input("Enter CourseID  to input Mark: "))
            if Input_Course_id in Course_id:
                mark = math.floor(float(input("mark: ")))
                Mark_List[i] = Mark(Input_Student_id, Input_Course_id, mark )
def Show_Mark():
    for i in range(nom):
        print(i + 1, " Mark Information : ")
        Mark_List[i].print()


def Caculate_GPA():
    sum_credit = 0
    for i in range(noc):
        sum_credit = Course_List[i].credit + sum_credit


    mark_credit_arr = np.zeros((nom))
    Input_Student_id_gpa = int(input("Enter StudentID to Caculate GPA: "))
    if Input_Student_id_gpa in Student_id:
        for i in range(nom):
            mark_credit_arr[i]=(Mark_List[i].mark * Course_List[i].credit)


    gpa = np.sum(mark_credit_arr)/sum_credit
    return gpa



def Show_GPA():
    for i in range (nos):
        print( "GPA of Student", i+1,": ", Caculate_GPA())










Student_List = []
Student_id = []

Course_List = []
Course_id = []

Mark_List = []

Number_of_Student()
Make_Student_List()
Student_Information()
Show_Student_Information()

Number_of_Course()
Make_Course_List()
Course_Information()
Show_Course_Information()

Number_of_Mark()
Make_Mark_List()
Input_Mark()
Show_Mark()

Show_GPA()