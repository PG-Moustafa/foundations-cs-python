import json

class Course:
    def __init__(self, code, name, credit_hours, is_core=True):
        self.code = code
        self.name = name
        self.credit_hours = credit_hours
        self.is_core = is_core

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "credit_hours": self.credit_hours,
            "is_core": self.is_core
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["code"], data["name"], data["credit_hours"], data["is_core"])

    def __str__(self):
        return f"{self.code} - {self.name} - {'Core' if self.is_core else 'Elective'}"

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = {}

    def enroll(self, course):
        if course.code in self.enrolled_courses:
            raise Exception(f"Already enrolled in {course.name}.")
        self.enrolled_courses[course.code] = course

    def drop(self, course_code):
        if course_code not in self.enrolled_courses:
            raise Exception(f"Not enrolled in course with code {course_code}.")
        del self.enrolled_courses[course_code]

    def list_courses(self):
        if not self.enrolled_courses:
            return "No courses enrolled."
        return "\n".join([str(course) for course in self.enrolled_courses.values()])

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "enrolled_courses": {code: course.to_dict() for code, course in self.enrolled_courses.items()}
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data["student_id"], data["name"])
        student.enrolled_courses = {code: Course.from_dict(course) for code, course in data["enrolled_courses"].items()}
        return student

class CourseCatalog:
    def __init__(self):
        self.courses = {}
        self.students = []

    def add_course(self, course):
        self.courses[course.code] = course

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def enroll_student_in_course(self, student_id, course_code):
        student = self.find_student(student_id)
        if not student:
            raise Exception(f"Student with ID {student_id} not found.")
        if course_code not in self.courses:
            raise Exception(f"Course with code {course_code} not found.")
        student.enroll(self.courses[course_code])

    def drop_student_from_course(self, student_id, course_code):
        student = self.find_student(student_id)
        if not student:
            raise Exception(f"Student with ID {student_id} not found.")
        student.drop(course_code)

    def list_student_courses(self, student_id):
        student = self.find_student(student_id)
        if not student:
            raise Exception(f"Student with ID {student_id} not found.")
        return student.list_courses()

    def to_dict(self):
        return {
            "courses": {code: course.to_dict() for code, course in self.courses.items()},
            "students": [student.to_dict() for student in self.students]
        }

    @classmethod
    def from_dict(cls, data):
        catalog = cls()
        catalog.courses = {code: Course.from_dict(course) for code, course in data["courses"].items()}
        catalog.students = [Student.from_dict(student) for student in data["students"]]
        return catalog

    def save_catalog(self, filename="course_catalog.json"):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f)
        print("Catalog saved successfully.")

    @classmethod
    def load_catalog(cls, filename="course_catalog.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                return cls.from_dict(data)
        except FileNotFoundError:
            print("No saved catalog found, starting a new one.")
            return cls()


def main():
    catalog = CourseCatalog.load_catalog()

    while True:
        print("\n--- Course Enrollment System ---")
        print("1. Add Course")
        print("2. Enroll Student in Course")
        print("3. Drop Course for Student")
        print("4. List Student Courses")
        print("5. Save Course Catalog")
        print("6. Load Course Catalog")
        print("7. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                code = input("Enter course code: ")
                name = input("Enter course name: ")
                credit_hours = int(input("Enter credit hours: "))
                is_core = input("Is this a core course? (yes/no): ").lower() == "yes"
                course = Course(code, name, credit_hours, is_core)
                catalog.add_course(course)
                print(f"Course {name} added.")

            elif choice == "2":
                student_id = input("Enter student ID: ")
                student_name = input("Enter student name: ")
                course_code = input("Enter course code: ")
                student = catalog.find_student(student_id)
                if not student:
                    student = Student(student_id, student_name)
                    catalog.students.append(student)
                catalog.enroll_student_in_course(student_id, course_code)
                print("Student enrolled in course.")

            elif choice == "3":
                student_id = input("Enter student ID: ")
                course_code = input("Enter course code to drop: ")
                catalog.drop_student_from_course(student_id, course_code)
                print("Course dropped for student.")

            elif choice == "4":
                student_id = input("Enter student ID: ")
                print("Courses enrolled:")
                print(catalog.list_student_courses(student_id))

            elif choice == "5":
                catalog.save_catalog()

            elif choice == "6":
                catalog = CourseCatalog.load_catalog()
                print("Catalog loaded.")

            elif choice == "7":
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"Error: {e}")

main()
