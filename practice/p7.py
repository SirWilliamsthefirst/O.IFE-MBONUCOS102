import random

class Employee:
    def __init__(self, employees):
        self.employees = employees
        self.attendance = set()

    def check_employee(self, name):
        if name in self.employees:
            return True
        else:
            return False

    def take_attendance(self, name):
        self.attendance.add(name)

    def assign_task(self):
        tasks = ["Loading", "Transporting", "Reviewing Orders", "Customer Service", "Delivering Items"]
        return random.choice(tasks)

    def refuse_access(self):
        print("Access Denied. You are not authorized to access the system.")

if __name__ == "__main__":
    employees = ["Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu", "Stella Mankinde",
                 "Jane Akibo", "Ago James", "Michell Taiwo", "Abraham Jones", "Nicole Anide", "Kosi Korso",
                 "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"]

    emp = Employee(employees)

    name = input("Enter your name: ")

    if name:
        if emp.check_employee(name):
            emp.take_attendance(name)
            task = emp.assign_task()
            print(f"Welcome, {name}")
            print(f"Your task for today is: {task}")
        else:
            emp.refuse_access()
    else:
        print("Please enter your name.")

