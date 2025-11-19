grades = {}

while True:
    print("\n========== STUDENT GRADE ANALYZER ==========\n1. Add student,\n2. View students\n3. Class average\n4. Highest grade\n5. Lowest grade\n6. Exit")
    choice = input("Choose an option: ").lower().strip()
    if choice == "1":
        name = input("Student name: ")
        grade = float(input("Grade: "))
        grades[name] = grade
        print(f"{name} added!")
    elif choice == "2":
        if grades:
            print("=============== STUDENTS ===============")
            for name, grade in grades.items():
                print(f"{name}:{grade}")
        else:
            print("No students have been added yet, try adding some :)")
    elif choice == "3":
        if grades:
            avg = sum(grades.values())/len(grades)
            print(f"Class average: {avg:.2f}")
        else:
            print("No data to calculate average, are you sure you added some students")
    elif choice == "4":
        if grades:
            top_student = max(grades, key=grades.get)
            print(f"The best Student is {top_student} with {grades[top_student]} for he's grades, give them a compliment will ya.;)")
        else:
            print("No data to calculate Best Student, it seems you forgot to add students before calculating the average")
    elif choice == "5":
        if grades:
            low_student = min(grades, key=grades.get)
            print(f"The worst student is {low_student} with {grades[low_student]} for he's grades, you should probably talk to them about this. :(")
        else:
            print(f"No data to calculate the Worst student, are you sure you added some students")
    elif choice == "6":
        print("GOOD BYE!!")
        break