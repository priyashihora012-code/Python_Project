from datetime import datetime
import time
import random
import uuid

from package.file_operation import *
from package.math import *

print()
print("=========================")
print("Welcome to Multi-Utility Toolkit")
print("=========================")

def show_menu():
    print("Choose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
   
def datetime_menu():

    print() 
    print("Datetime and Time Operations:")
    print("1. Display current date and time")
    print("2. Calculate difference between two dates/times")
    print("3. Format date into custom format")
    print("4. Stopwatch")
    print("5. Countdown Timer")
    print("6. Back to Main Menu")

    while True:
      
        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            print("Current Date and Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("=========================")

        elif choice == "2":
            d1 = input("Enter the first date (YYYY-MM-DD): ")
            d2 = input("Enter the second date (YYYY-MM-DD): ")
            a = datetime.strptime(d1, "%Y-%m-%d")
            b = datetime.strptime(d2, "%Y-%m-%d")
            diff = abs((b - a).days)
            print("Difference:", diff, "days")
            print("=========================")

        elif choice == "3":
            d = input("Enter date (YYYY-MM-DD): ")
            dt = datetime.strptime(d, "%Y-%m-%d")
            print("Formatted Date:", dt.strftime("%d-%m-%Y"))
            print("=========================")

        elif choice == "4":
            input("Press Enter to start stopwatch...")
            s = time.time()
            input("Press Enter to stop stopwatch...")
            e = time.time()
            print("Elapsed Time:", round(e - s, 2), "seconds")
            print("=========================")

        elif choice == "5":
            n = int(input("Enter countdown seconds: "))
            for i in range(n, 0, -1):
                print(i)
                time.sleep(1)
            print("Time's up!")
            print("=========================")

        elif choice == "6":
            break
        else:
            print("Invalid choice")

def math_menu():

    print()
    print("Mathematical Operations:")
    print("1. Calculate Factorial")
    print("2. Solve Compound Interest")
    print("3. Trigonometric Calculations")
    print("4. Area of Geometric Shapes")
    print("5. Back to Main Menu")

    while True:
        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            n = int(input("Enter a number: "))
            print("Factorial:", factorial(n))
            print("=========================")

        elif choice == "2":
            p = float(input("Enter principal amount: "))
            r = float(input("Enter rate of interest (in %): "))
            t = float(input("Enter time (in years): "))
            print("Compound Interest:", compound_interest(p, r, t))
            print("=========================")

        elif choice == "3":
            angle = float(input("Enter angle in degrees: "))
            print("Trigonometric Values:", trig_values(angle))
            print("=========================")

        elif choice == "4":
            print("1. Circle")
            print("2. Rectangle")
            ch = input("Choose shape: ")
            if ch == "1":
                r = float(input("Enter radius: "))
                print("Area of Circle:", area_circle(r))
            elif ch == "2":
                l = float(input("Enter length: "))
                w = float(input("Enter width: "))
                print("Area of Rectangle:", area_rectangle(l, w))
                print("=========================")

        elif choice == "5":
            break
        else:
            print("Invalid choice")

def random_menu():

    print()
    print("Random Data Generation:")
    print("1. Generate Random Number")
    print("2. Generate Random List")
    print("3. Create Random Password")
    print("4. Generate Random OTP")
    print("5. Back to Main Menu")
       
    while True:
      
        choice = input("Enter your choice: ")
        print()
        if choice == "1":
            s = int(input("Enter start: "))
            e = int(input("Enter end: "))
            print("Random Number:", random.randint(s, e))
            print("=========================")

        elif choice == "2":
            count = int(input("Enter how many numbers: "))
            s = int(input("Enter start: "))
            e = int(input("Enter end: "))
            lst = []
            for _ in range(count):
                lst.append(random.randint(s, e))
            print("Random List:", lst)
            print("=========================")

        elif choice == "3":
            length = int(input("Enter password length: "))
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%&*"
            pwd = ""
            for _ in range(length):
                pwd += random.choice(chars)
            print("Generated Password:", pwd)
            print("=========================")

        elif choice == "4":
            print("Generated OTP:", random.randint(100000, 999999))
            print("=========================")

        elif choice == "5":
            break
        else:
            print("Invalid choice")

def uuid_menu():

    print()
    print("Generate Unique Identifiers (UUID):")
    print("Generated UUID:", uuid.uuid4())
    print("=========================")

def file_menu():

    print()
    print("File Operations (Custom Module):")
    print("1. Create a new file")
    print("2. Write to a file")
    print("3. Read from a file")
    print("4. Append to a file")
    print("5. Back to Main Menu")
    
    while True:
        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            fname = input("Enter file name: ")
            print(create_file(fname))
            print("=========================")

        elif choice == "2":
            fname = input("Enter file name: ")
            data = input("Enter data to write: ")
            print(write_file(fname, data))
            print("=========================")

        elif choice == "3":
            fname = input("Enter file name: ")
            print("File Content:")
            print(read_file(fname))
            print("=========================")

        elif choice == "4":
            fname = input("Enter file name: ")
            data = input("Enter data to append: ")
            print(append_file(fname, data))
            print("=========================")

        elif choice == "5":
            break
        else:
            print("Invalid choice")

def explore_module():
    print()
    print("Explore Module Attributes (dir()):")
    mname = input("Enter module name to explore: ")
    try:
        m = __import__(mname)
        print("Available Attributes in", mname, "module:")
        print(dir(m))
        print()
    except:
        print("Module not found!")
        print()

def main():

    while True:

        show_menu()
        choice = input("Enter your choice: ")
       
        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_module()
        elif choice == "7":
            print()
            print("=========================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("=========================")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()