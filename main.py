class Student:
    __attendance = 0

    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa

    def display(self):
        print(self.name, self.student_id, self.gpa)

    @classmethod
    def get_attendance(cls):
        return cls.__attendance

    @classmethod
    def mark_attendance(cls):
        cls.__attendance += 1  # Modify class attribute

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []
        self.student_count = 0

    def add_student(self, student):
        if isinstance(student, Student):  # Ensure student is valid
            self.students.append(student)
            self.student_count += 1


    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.student_count -= 1

    def list_students(self):
        for student in self.students:
            print("Name: "+ student.name + " \n")


student1 = Student("alice", "512345", 3.8)
student2 = Student("bob", "567890", 3.5)

course = Course("computer science")
course.add_student(student1)
course.add_student(student2)

course.list_students()
student1.mark_attendance()
print("Attendance for Alice:", student1.get_attendance())
