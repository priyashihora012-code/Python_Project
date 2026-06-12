class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def __del__(self):
        pass

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary


    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary: $", self.__salary, sep="")


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        print("Manager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary(), sep="")
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        print("Developer Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary(), sep="")
        print("Programming Language:", self.programming_language)


person = None
employee = None
manager = None

print("\n--- Python OOP Project: Employee Management System ---")

while True:
    
    print("Choose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))

            person = Person(name, age)

            print(f"Person created with name: {name} and age: {age}.")

        case "2":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))

            employee = Employee(name, age, emp_id, salary)

            print(f"Employee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary}.")

        case "3":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")

            manager = Manager(name, age, emp_id, salary, department)

            print(f"Manager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and department: {department}.")

        case "4":
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")

            option = input("Enter your choice: ")

            match option:

                case "1":
                    if person:
                        person.display()
                    else:
                        print("No Person record found.")

                case "2":
                    if employee:
                        employee.display()
                    else:
                        print("No Employee record found.")

                case "3":
                    if manager:
                        manager.display()
                    else:
                        print("No Manager record found.")

                case _:
                    print("Invalid choice.")

        case "5":
            print("\nExiting the system. All resources have been freed.")
            print("Goodbye!")
            break

        case _:
            print("Invalid choice.")

    print("\nChoose another operation")