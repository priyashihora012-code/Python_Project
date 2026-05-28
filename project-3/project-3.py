students = []        
all_subjects = set() 

print("Welcome to the Student Data Organizer!")

while True:

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":  # ADD STUDENT
       
            print("\nEnter student details:")
            student_id = input("Student ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subjects_input = input("Subjects (comma-separated) : ")

            subjects = set(s.strip() for s in subjects_input.split(","))

            id_dob = (student_id, dob)

            student = {
                "student_id": student_id,
                "name": name,
                "age": age,
                "grade": grade,
                "subjects": subjects,
                "id_dob": id_dob
            }

            students.append(student)
            all_subjects.update(subjects)

            print("\nStudent added successfully!")

        case "2":  # DISPLAY ALL STUDENTS
      
            print("\n--- Display All Students ---")

            if len(students) == 0:
                print("No student records found.")
            else:
                for s in students:
                    subjects_str = ", ".join(sorted(s["subjects"]))
                    print(f"Student ID: {s['id_dob'][0]} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']} | Subjects: {subjects_str}")

        case "3":  # UPDATE STUDENT
       
            print("\n--- Update Student Information ---")
            student_id = input("Enter Student ID to update: ")

            found = None
            for s in students:
                if s["student_id"] == student_id:
                    found = s
                    break

            if found is None:
                print("Student not found.")
            else:
                print(f"Updating: {found['name']}")
                print("1. Age  2. Grade  3. Subjects")
                update_choice = input("Enter your choice: ")

                match update_choice:
                    case "1":
                        found["age"] = int(input("Enter new age: "))
                        print("Age updated successfully!")
                    case "2":
                        found["grade"] = input("Enter new grade: ")
                        print("Grade updated successfully!")
                    case "3":
                        new_subjects = set(s.strip() for s in input("Enter new subjects: ").split(","))
                        found["subjects"] = new_subjects
                        all_subjects.update(new_subjects)
                        print("Subjects updated successfully!")
                    case _:
                        print("Invalid choice.")

        case "4":  # DELETE STUDENT
    
            print("\n--- Delete Student ---")
            student_id = input("Enter Student ID to delete: ")

            deleted = False
            for i in range(len(students)):
                if students[i]["student_id"] == student_id:
                    del students[i]
                    print(f"Student with ID '{student_id}' deleted successfully!")
                    deleted = True
                    break

            if not deleted:
                print("Student not found.")

        case "5":  # DISPLAY SUBJECTS
       
            print("\n--- Display Subjects Offered ---")

            if len(all_subjects) == 0:
                print("No subjects found.")
            else:
                print("Subjects offered: " + ", ".join(sorted(all_subjects)))

        
        case "6": # EXIT
            print("\nThank you for using the Student Data Organizer. Goodbye!")
            break

        case _:  
            print("Invalid choice! Please enter a number between 1 and 6.")

