# Hämtar funktionerna från student
from student import create_new_student, save_students, read_students, show_all_students
from student import add_course, show_student, remove_course , remove_student
# Hämtar funktionerna från todo
from todo import add_todo, get_most_urgent, get_first_todo, save_todos
from todo import delete_todo, get_all_todos_string, read_todos
# Hämtar funktioner från event
from event import create_event, add_participants_to_event, get_event
from event import get_participants, save_events, read_events


def setup():

    read_events()
    read_students()
    read_todos()

def save():

    save_events()
    save_students()
    save_todos()

def main():
    setup()
    main_menu()
    

def main_menu():

    print("Welcome to the School Administration!")
    
    while True:
        print("Main Menu\n"
              "1. Student Menu\n"
              "2. Event Menu\n"
              "3. ToDo Menu\n"
              "4. Quit\n")
        
        choice = input("Make a choice:\n>> ")
        print("")

        if choice == "1":
            student_menu()

        elif choice == "2":
            event_menu()

        elif choice == "3":
            todo_menu()

        elif choice == "4":
            print("Goodbye User!")
            break

        else:
            print("Incorrect Input!\n")

def student_menu():
    while True:
        print("Student Menu\n" \
        "1. Add student\n"
        "2. Remove student\n" \
        "3. View one student\n"
        "4. Show all students\n" \
        "5. Add course\n" \
        "6. Remove course\n"
        "7. Back to main menu\n")
        choice = input("Make a choice:\n>> ")
        print("")

        if choice == "1":
            create_new_student()

        elif choice == "2":
            remove_student()

        elif choice == "3":
            show_student()

        elif choice == "4":
            show_all_students()

        elif choice == "5":
            add_course()

        elif choice == "6":
            remove_course()

        elif choice == "7":
            break

        else:
            print("Incorrect Input!\n")


def event_menu():
    ...

def todo_menu():
    ...


if __name__ == "__main__":
    main()