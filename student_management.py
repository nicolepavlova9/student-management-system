students = {1: {'name': 'Nicole', 'age': 23, 'grade': 5.5, 'subjects': ['Math', ' History']},
            2: {'name': 'Ivailo', 'age': 23, 'grade': 5.5, 'subjects': ['Math', ' History']},
            3: {'name': 'HelloTest', 'age': 10, 'grade': 3.4, 'subjects': ['Test1', ' Test2']},
            4: {'name': 'Nicole', 'age': 10, 'grade': 3.4, 'subjects': ['Test1', ' Test2']}}


def add_student(name, age, grade, subjects):
    # Determine the next key for the new student
    # If the students dictionary is empty, start with key 1
    if not students:
        current_key = 1
    else:
        # Otherwise, use the next key by incrementing the last key
        current_key = list(students)[-1] + 1
    new_student = {'name': name, 'age': age, 'grade': grade, 'subjects': subjects}
    students[current_key] = new_student


def update_student(name):
    student_found = None
    for key, value in students.items():
        if value['name'] == name:
            student_found = True
            print('\nChoose your option:')
            print('1. Update Name')
            print('2. Update Age')
            print('3. Update Grade')
            print('4. Update Subjects')
            option = int(input('Enter the number of the option you want to update: '))
            if option == 1:
                new_name = input('Choose a new name: ')
                students[key]['name'] = new_name
            elif option == 2:
                new_age = int(input('Choose the new age: '))
                students[key]['age'] = new_age
            elif option == 3:
                new_grade = float(input('Choose the new grade: '))
                students[key]['grade'] = new_grade
            elif option == 4:
                new_subjects = input("Enter the new subjects, separated by commas: ").split(',')
                students[key]['subjects'] = new_subjects
            break
    if not student_found:
        print('Student not found!')


def delete_student(name):
    student_found = None
    for key, value in students.items():
        if value['name'] == name:
            student_found = True
            students.pop(key)
            break
    if not student_found:
        print('\nStudent not found!')


def search_student(name):
    pass
    # student_found = None
    # for key, value in students.items():
    #     if value['name'] == name:
    #         student_found = True
    #         break
    # if not student_found:
    #     print('No student found.')


def list_all_students():
    """
    List all student records.
    """
    # Check if there are any student records
    # Code to list all students


def main():
    """
    Main function to provide user interaction.
    """
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for student details
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = float(input("Enter student's grade: "))
            subjects = input("Enter student's subjects (comma-separated): ").split(',')
            # Call the add_student function
            add_student(name, age, grade, subjects)
        elif choice == '2':
            # Prompt for student name to update
            name = input("Enter student's name to update: ")
            # Call the update_student function
            update_student(name)
        elif choice == '3':
            # Prompt for student name to delete
            name = input("Enter student's name to delete: ")
            # Call the delete_student function
            delete_student(name)
        elif choice == '4':
            # Prompt for student name to search
            name = input("Enter student's name to search: ")
            # Call the search_student function
            search_student(name)
        elif choice == '5':
            # Call the list_all_students function
            list_all_students()
        elif choice == '6':
            # Exit the program
            break
        else:
            print("Invalid choice, please try again.")


#
# if __name__ == "__main__":
#     main()
