
def Number_of_Student():
    global nos
    nos = int(input("Number of Students: "))
    return nos


def Student_Information():
    for i in range (0, nos):
        print("Enter Student Information: ")
        id = input("ID: ")
        name = input("Name : ")
        DoB = input("DoB: ")
        Student_List.append([id,name,DoB])
        Student_id.append(id)

def Number_of_Course():
    global noc
    noc = int(input("Number of Course: "))
    return noc


def Course_Information():
    for i in range (0, noc):
        print("Enter Course Information: ")
        id = input("ID: ")
        name = input("Name : ")
        Course_List.append([id,name])
        Course_id.append(id)

def Input_Mark():
    Input_Student_id = input("Enter StudentID to input Mark: ")
    if Input_Student_id in Student_id:
        Input_Course_id = input("Enter CourseID  to input Mark: ")
        if Input_Course_id in Course_id:
            mark = int(input("mark: "))
    print("Student ID: ", Input_Student_id, "Course ID: ", Input_Course_id, "mark:", mark)


#main
Student_List = []
Student_id = []
Course_List = []
Course_id = []
Number_of_Student()
Student_Information()
print(Student_List)
Number_of_Course()
Course_Information()
print(Course_List)
Input_Mark()


