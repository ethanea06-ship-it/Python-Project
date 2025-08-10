#Fragment 1.1

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

#Fragment 1.2

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


#Fragment 1.3

# --- Front Desk Functions ---
def find_student_by_id(student_id):
    """A new helper to find one student by their exact ID."""
    for student in student_db:
        if student.id == student_id:
            return student
    return None

def front_desk_register(name, instrument):
    """High-level function to register a new student and enrol them."""
    global next_student_id
    new_student = Student(next_student_id, name)
    student_db.append(new_student)
    next_student_id += 1
    
    # Enroll the student in their first instrument
    front_desk_enrol(new_student.id, instrument)
    print(f"Front Desk: Successfully registered '{name}' and enrolled them in '{instrument}'.")
    return new_student

def front_desk_enrol(student_id, instrument):
    """High-level function to enrol an existing student in a course."""
    student = find_student_by_id(student_id)
    if student:
        student.enrolled_in.append(instrument)
        print(f"Front Desk: Enrolled student {student_id} in '{instrument}'.")
        return True
    else:
        print(f"Error: Student ID {student_id} not found.")
        return False

def front_desk_lookup(term):
    """High-level function to search everything."""
    print(f"\n--- Performing lookup for '{term}' ---")
    find_students(term)
    find_teachers(term)

#Fragment 1.4
# --- Main Application ---
def main():
    """Runs the main interactive menu for the receptionist."""
    # Pre-populate some data for easy testing
    add_teacher("Dr. Keys", "Piano")
    add_teacher("Ms. Fret", "Guitar")
    front_desk_register("Sample Student", "Violin")  # Add a sample student

    while True:
        print("\n===== Music School Front Desk =====")
        print("1. Register New Student")
        print("2. Enrol Existing Student")
        print("3. Lookup Student or Teacher")
        print("4. (Admin) List all Students")
        print("5. (Admin) List all Teachers")
        print("q. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            instrument = input("Enter instrument to enrol in: ")
            front_desk_register(name, instrument)
            
        elif choice == '2':
            try:
                student_id = int(input("Enter student ID: "))
                instrument = input("Enter instrument to enrol in: ")
                front_desk_enrol(student_id, instrument)
            except ValueError:
                print("Invalid ID. Please enter a number.")
                
        elif choice == '3':
            term = input("Enter search term: ")
            front_desk_lookup(term)
            
        elif choice == '4':
            list_students()
            
        elif choice == '5':
            list_teachers()
            
        elif choice.lower() == 'q':
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

# --- Program Start ---
if __name__ == "__main__":
    main()