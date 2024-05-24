students = {}


def add_student(name, age, grade, subjects):
    current_key = max(students.keys(), default=0) + 1
    new_student = {'name': name, 'age': age, 'grade': grade, 'subjects': subjects}
    students[current_key] = new_student


def update_student(name):
    student_found = False
    for key, value in students.items():
        if value['name'].lower() == name.lower():
            student_found = True
            print('\nChoose your option:')
            print('1. Update Name')
            print('2. Update Age')
            print('3. Update Grade')
            print('4. Update Subjects')
            option = int(input('Enter the number of the option you want to update: '))
            if option == 1:
                try:
                    new_name = input('Choose a new name: ')
                    if new_name.isalpha():
                        students[key]['name'] = new_name
                        print(f"Name updated to {new_name}")
                    else:
                        raise ValueError('\nInvalid name. Names must contain only alphabetic characters.')
                except ValueError as error_message:
                    print(error_message)
            elif option == 2:
                try:
                    new_age = input('Choose the new age: ')
                    if new_age.isdigit() and 0 < int(new_age) < 99:
                        students[key]['age'] = new_age
                        print(f'Student {students[key]["name"]} age changed to {new_age}')
                    else:
                        raise ValueError('\nInvalid age, please use only a positive number and no bigger than 99.')
                except ValueError as error_message:
                    print(error_message)
            elif option == 3:
                try:
                    new_grade = float(input('Choose the new grade: '))
                    if 2.0 <= new_grade <= 6.0:
                        students[key]['grade'] = new_grade
                        print(f'Student {students[key]["name"]} grade changed to {new_grade}')
                    else:
                        print('\nInvalid grade. Please use only numbers from 2.00 to 6.00')
                except ValueError:
                    print('\nInvalid input. Please enter a numeric value for the grade.')
            elif option == 4:
                new_subjects_input = input("Enter the new subjects, separated by commas: ")
                new_subjects = [subject.strip() for subject in new_subjects_input.split(',')]
                if all(subject.isalpha() for subject in new_subjects) and new_subjects:
                    students[key]['subjects'] = new_subjects
                    print(f"Subjects updated to: {', '.join(new_subjects)}")
                else:
                    print(
                        '\nInvalid subjects. Each subject must contain only alphabetic characters and cannot be empty.')
            else:
                print('Invalid option.')
    if not student_found:
        print('\nStudent not found!')


def delete_student(name):
    student_found = False
    for key, value in students.items():
        if value['name'].lower() == name.lower():
            student_found = True
            students.pop(key)
            break
    if not student_found:
        print('\nStudent not found!')


def search_student(name):
    student_found = False
    for key, value in students.items():
        if value['name'].lower() == name.lower():
            student_found = True
            print('\n----------')
            print(f'Student name: {students[key]["name"]}')
            print(f'Student age: {students[key]["age"]}')
            print(f'Student grade: {students[key]["grade"]}')
            print(f'Student subjects:', ', '.join(subject.strip() for subject in value['subjects']))
            print('----------')
    if not student_found:
        print('\nStudent not found!')


def list_all_students():
    if not students:
        print('No students found.')
    else:
        for key, value in students.items():
            print('\n----------')
            print(f'Student name: {students[key]["name"]}')
            print(f'Student age: {students[key]["age"]}')
            print(f'Student grade: {students[key]["grade"]}')
            print(f'Student subjects:', ', '.join(subject.strip() for subject in value['subjects']))
            print('----------')


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
if __name__ == "__main__":
    main()
