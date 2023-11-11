# Function to search for a specific student record by ID
def search_by_id(id):
    with open("student_records.txt", "r") as file:
        for line in file:
            data = line.strip().split(',')
            if data[1] == id:
                print(f"Student found: {data[0]} - ID: {data[1]}, Grade: {data[2]}")
                return True
        return False

# Function to add student details to the file
def add_student(name, id, grade):
    with open("student_records.txt", "a") as file:
        if search_by_id(id):
            print("Student already exists")
            return
        file.write(f"{name},{id},{grade}\n")
    print("Student added successfully.")

# Function to display all student records from the file
def display_students():
    with open("student_records.txt", "r") as file:
        print("Student Records:")
        print(file.read())

# Menu for user interaction
def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            grade = input("Enter student's grade: ")
            add_student(name, student_id, grade)
        elif choice == '2':
            display_students()
        elif choice == '3':
            student_id = input("Enter student ID to search: ")
            search_by_id(student_id)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")

# Run the main function
if __name__ == "__main__":
    main()
