from abc import ABC, abstractmethod


class Employee_Payroll_System(ABC):

    def __init__(self, name, id, role):
        self.name = name
        self.id = id
        self.role = role

    @abstractmethod
    def salary_calculate(self):
        pass

    @abstractmethod
    def genrate_payslip(self):
        pass
class FullTimeEmployee(Employee_Payroll_System):

    def __init__(self, name, id, role, sal):
        super().__init__(name, id, role)
        self.sal = sal

    def salary_calculate(self):

        print(f"Full time salary = {self.sal}")

    def tax_deduction(self):

        self.sal -= 2000
        print("After tax:", self.sal)

    def genrate_payslip(self):

        print("| name | id | salary | role |")
        print("----------------------------")
        print(f"{self.name} {self.id} {self.sal} {self.role}")
class PartTimeEmployee(Employee_Payroll_System):

    def __init__(self, name, id, role, hour):
        super().__init__(name, id, role)
        self.hour = hour
        self.sal = 0

    def salary_calculate(self):

        self.sal = self.hour * 500
        print("Part time salary =", self.sal)

    def tax_deduction(self):

        self.sal -= 1000
        print("After tax:", self.sal)

    def genrate_payslip(self):

        print("| name | id | salary | role |")
        print("----------------------------")
        print(f"{self.name} {self.id} {self.sal} {self.role}")
emp = None

while True:

    print("""
1 Full Time Employee
2 Part Time Employee
3 Calculate Salary
4 Tax Deduction
5 Payslip
6 Exit
""")

    ch = input("Choice: ")

    match ch:

        case "1":

            name = input("Name: ")
            id = input("ID: ")
            sal = int(input("Salary: "))

            emp = FullTimeEmployee(name, id, "fulltime", sal)

        case "2":

            name = input("Name: ")
            id = input("ID: ")
            hour = int(input("Hours: "))

            emp = PartTimeEmployee(name, id, "parttime", hour)

        case "3":

            if emp:
                emp.salary_calculate()

        case "4":

            if emp:
                emp.tax_deduction()

        case "5":

            if emp:
                emp.genrate_payslip()

        case "6":

            break

        case _:

            print("Invalid")