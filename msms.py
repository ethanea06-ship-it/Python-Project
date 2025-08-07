class Student:
    def __init__(self,student_id, name):
        self.id = student_id
        self.name = name 
# empty list (enrolled in stores names)
        self.enrolled_in = []

class Teacher:
    def __init__(self,teacher_id,name,specialty):
    #define each variable
        self.id = teacher_id
        self.name = name 
        self.specialty = specialty
        
#memory database
student_db = []
teacher_db = []
next_student_id = 1
next_teacher_id = 2

