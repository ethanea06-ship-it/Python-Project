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


def add_teacher(name, speciality):
    """Creates a Teacher object and adds it to the database."""
    global next_teacher_id
    new_teacher = Teacher(next_teacher_id, name, speciality)
    teacher_db.append(new_teacher)
    next_teacher_id += 1
    print(f"Core: Teacher '{name}' added successfully.")

def list_students():
    """Prints all students in the database."""
    print("\n--- Student List ---")
    if not student_db:
        print("No students in the system.")
        return
    for student in student_db:
        instruments = ', '.join(student.enrolled_in) if student.enrolled_in else "None"
        print(f"  ID: {student.id}, Name: {student.name}, Enrolled in: {instruments}")

def list_teachers():
    """Prints all teachers in the database."""
    print("\n--- Teacher List ---")
    if not teacher_db:
        print("No teachers in the system.")
        return
    for teacher in teacher_db:
        print(f"  ID: {teacher.id}, Name: {teacher.name}, Speciality: {teacher.speciality}")

def find_students(term):
    """Finds students by name."""
    print(f"\n--- Finding Students matching '{term}' ---")
    results = []
    term = term.lower()  # Make search case-insensitive
    for student in student_db:
        if term in student.name.lower():
            results.append(student)
    
    if not results:
        print("No matching students found.")
    else:
        for student in results:
            instruments = ', '.join(student.enrolled_in) if student.enrolled_in else "None"
            print(f"  ID: {student.id}, Name: {student.name}, Enrolled in: {instruments}")

def find_teachers(term):
    """Finds teachers by name or speciality."""
    print(f"\n--- Finding Teachers matching '{term}' ---")
    results = []
    term = term.lower()  # Make search case-insensitive
    for teacher in teacher_db:
        if (term in teacher.name.lower()) or (term in teacher.speciality.lower()):
            results.append(teacher)
    
    if not results:
        print("No matching teachers found.")
    else:
        for teacher in results:
            print(f"  ID: {teacher.id}, Name: {teacher.name}, Speciality: {teacher.speciality}")
            