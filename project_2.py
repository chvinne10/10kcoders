class Student_Management_System:

    def __init__(self):
        self.student = {}
        self.subject = {}
        self.marks = {}

    def add_student(self, id, name, age):

        self.student[id] = {
            'name': name,
            'age': age,
        }

    def Enroll_course(self, id, no_subject):

        self.subject[id] = {}

        for i in range(no_subject):
            self.subject[id][i] = input("Enter subject: ")

    def add_marks(self, id, no_subject):

        self.marks[id] = {}

        for i in range(no_subject):
            self.marks[id][i] = int(input("Enter marks: "))

    def cal_grade(self, id, subject):

        avg = 0

        for i in range(subject):
            avg += self.marks[id][i]

        grade = avg / subject

        if grade > 90:
            return "Great"
        elif grade > 80:
            return "Good"
        elif grade > 50:
            return "Average"
        else:
            return "Poor"

    def view_student_details(self, id):

        print("| Subject | Marks |")
        print("-------------------")

        for i in range(len(self.subject[id])):
            print(
                f"| {self.subject[id][i]} | {self.marks[id][i]} |"
            )

        print("Total Grade:")
        print(self.cal_grade(id, len(self.subject[id])))
sms = Student_Management_System()

while True:

    print("1 Add Student\n2 Enroll Course\n3 Add Marks\n4 View Student\nExit")

    ch = input("Enter choice: ")

    match ch:

        case "1":

            id = input("Enter id: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))

            sms.add_student(id, name, age)

        case "2":

            id = input("Enter id: ")
            n = int(input("No of subjects: "))

            sms.Enroll_course(id, n)

        case "3":

            id = input("Enter id: ")
            n = int(input("No of subjects: "))

            sms.add_marks(id, n)

        case "4":

            id = input("Enter id: ")

            sms.view_student_details(id)

        case "5":

            break

        case _:

            print("Invalid choice")