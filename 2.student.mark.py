
class Student:

    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB

    def print(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("DoB", self.DoB)

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
        print(i+1, " Student Informations : ")
        Student_List[i].print()





class Course:

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def print(self):
        print("ID:", self.id)
        print("Name:", self.name)

def Number_of_Course():
    global noc
    noc = int(input("Number of Course: "))
    return noc

def Make_Course_List():
    for i in range(noc):
        Course_List.append(i)

def Course_Information():
    for i in range (nos):
        print("Enter Course Information: ")
        Course_List[i] = Course(int(input("id:")),input("name: "))
        Course_id.append(Course_List[i].id)

def Show_Course_Information():
    for i in range (nos):
        print( i+1 ," Course Informations : ")
        Course_List[i].print()


def Input_Mark():
    global Input_Course_id, mark
    Input_Student_id = int(input("Enter StudentID to input Mark: "))
    if Input_Student_id in Student_id:
        Input_Course_id = int(input("Enter CourseID  to input Mark: "))
        if Input_Course_id in Course_id:
            mark = int(input("mark: "))
    print("Student ID:", Input_Student_id, "Course ID:", Input_Course_id, "mark:", mark)

Student_List = []
Student_id = []
Course_List = []
Course_id = []

Number_of_Student()
Make_Student_List()
Student_Information()
Show_Student_Information()

Number_of_Course()
Make_Course_List()
Course_Information()
Show_Course_Information()

Input_Mark()

