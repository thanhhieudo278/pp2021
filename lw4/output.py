

def Show_Student_Information():
    for i in range (nos):
        print(i+1, " Student Information : ")
        Student_List[i].print()


def Show_Course_Information():
    for i in range (nos):
        print( i+1 ," Course Information : ")
        Course_List[i].print()


def Show_Mark():
    for i in range(nom):
        print(i + 1, " Mark Information : ")
        Mark_List[i].print()

def Show_GPA():
    for i in range (nos):
        print( "GPA of Student", i+1,": ", Caculate_GPA())
