from pathlib import Path  

DATA_FILE = Path(__file__).resolve().parent / "nisha.txt"


def read_students():
    students = []
    if not DATA_FILE.exists():
        return students
    with DATA_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = [part.strip() for part in line.split(",", 2)]
            if len(parts) == 3:
                students.append(parts)
    return students


def add_student():
    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()
    cgpa = input("Enter CGPA: ").strip()
    with DATA_FILE.open("a", encoding="utf-8") as f:
        f.write(f"{name},{course},{cgpa}\n")
    print("Student added.")


def view_students():
    students = read_students()
    if not students:
        print("No students found.")
        return
    for name, course, cgpa in students:
        print("Name:", name, "Course:", course, "CGPA:", cgpa)


def search_student():
    search_name = input("Enter student name: ").strip().lower()
    if not search_name:
        print("Please enter a name.")
        return
    students = read_students()
    if not students:
        print("No student records yet.")
        return
    results = [s for s in students if search_name in s[0].lower()]
    if not results:
        print("Student not found.")
        return
    for name, course, cgpa in results:
        print("Student found:")
        print("Name:", name)
        print("Course:", course)
        print("CGPA:", cgpa)


def update_student():
    students = read_students()
    if not students:
        print("No student records yet.")
        return
    search_name = input("Enter student name to update: ").strip().lower()
    updated = False
    for i, (name, course, cgpa) in enumerate(students):
        if search_name == name.lower():
            print("Current details:", name, course, cgpa)
            new_course = input("Enter new course (leave blank to keep current): ").strip()
            new_cgpa = input("Enter new CGPA (leave blank to keep current): ").strip()
            if new_course:
                course = new_course
            if new_cgpa:
                cgpa = new_cgpa
            students[i] = [name, course, cgpa]
            updated = True
            break
    if updated:
        with DATA_FILE.open("w", encoding="utf-8") as f:
            for s in students:
                f.write(",".join(s) + "\n")
        print("Student updated successfully.")
    else:
        print("Student not found.")


def delete_student():
    students = read_students()
    if not students:
        print("No student records yet.")
        return
    search_name = input("Enter student name to delete: ").strip().lower()
    new_students = [s for s in students if s[0].lower() != search_name]
    if len(new_students) == len(students):
        print("Student not found.")
    else:
        with DATA_FILE.open("w", encoding="utf-8") as f:
            for s in new_students:
                f.write(",".join(s) + "\n")
        print("Student deleted successfully.")


def show_statistics():
    students = read_students()
    if not students:
        print("No student records yet.")
        return
    cgpas = [float(s[2]) for s in students if s[2].replace('.', '', 1).isdigit()]
    if not cgpas:
        print("No valid CGPA data.")
        return
    print("Average CGPA:", sum(cgpas) / len(cgpas))
    print("Highest CGPA:", max(cgpas))
    print("Lowest CGPA:", min(cgpas))


def count_students():
    print("Total students:", len(read_students()))


while True:
    print("\n1 Add student")
    print("2 View students")
    print("3 Search student")
    print("4 Count students")
    print("5 Update student")
    print("6 Delete student")
    print("7 Show statistics")
    print("8 Exit")
    choice = input("Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        count_students()
    elif choice == "5":
        update_student()
    elif choice == "6":
        delete_student()
    elif choice == "7":
        show_statistics()
    elif choice == "8":
        print("Bye.")
        break
    else:
        print("Invalid choice.")

