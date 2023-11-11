import ex_06

def student_mean(x):
    sum = 0
    count = 0
    for item in x:
        sum += item
        count += 1
    return sum / count

def student_median(x):
    x.sort()
    if len(x) % 2 == 0:
        middle_index = int(len(x) / 2)
        num_1 = x[middle_index]
        num_2 = x[middle_index + 1]
        median = (num_1 + num_2) / 2
        return median
    else:
        middle_index = int((len(x) + 1 ) / 2)
        median = x[middle_index]
        return median

def student_mode(x):
    count_high = 0
    count_num = 0
    for num in x:
        if count_high < x.count(num):
            count_high = x.count(num)
            count_num = num
    if count_high == 0 or count_high == 1:
        return 0
    else:
        return count_num


def student_range(x):
    x.sort()
    min_value = x[0]
    max_value = x[-1]
    return max_value - min_value


def student_data():
    data_arr = []
    with open("student_records.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            data_arr.append(int(data[2]))
        return data_arr

def grading_system(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"

def student_grade(id):
    with open("student_records.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[1] == id:
                return grading_system(int(data[2]))
        print("Student could not be found.")
        return ""

def no_that_passed():
    student_arr = student_data()
    count = 0
    if len(student_arr) == 0: # Can replace with 'if student_arr.isempty()'
        print("There are no students available.")
        return 0
    else:
        for score in student_arr:
            if score >= 50:
                count += 1
    return count

def copy_contents(filename):
    with open("student_records.txt", "r") as read_file:
        with open(filename, "a") as copy_file:
            for line in read_file:
                data = line.strip().split(",")
                copy_file.write(f"{data[0]},{data[1]},{grading_system(int(data[2]))}\n")
        print(f"Data copied to {filename} successfully.")


# def main():
while True:
    print("\nStudent Grade Management System")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Get Student Analytics")
    print("5. Check Student Grades")
    print("6. Copy Data with grades to New File")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == '1':
        name = input("Enter student's name: ")
        student_id = input("Enter student's ID: ")
        grade = input("Enter student's grade: ")
        ex_06.add_student(name, student_id, grade)
    elif choice == '2':
        ex_06.display_students()
    elif choice == '3':
        student_id = input("Enter student ID to search: ")
        ex_06.search_by_id(student_id)
    elif choice == '4':
        print("Student Analytics")
        print(f"Mean: {student_mean(student_data())}")
        print(f"Median: {student_median(student_data())}")
        print(f"Mode: {student_mode(student_data())}")
        print(f"Range: {student_range(student_data())}")
        print(f"Number of students that passed: {no_that_passed()}")
    elif choice == '5':
        student_id = input("Enter student ID to search: ")
        grade = student_grade(student_id)
        if not grade == "":
            print(f"Student Grade: {grade}")
    elif choice == '6':
        filename = input("Enter file name to copy data into: ")
        copy_contents(filename)
    elif choice == '7':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")

# if __name__ == "__main__":
#     main()