import curses
import numpy as np
import math
from domains import Student
from domains import Course
from domains import Mark

Student.Student
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

