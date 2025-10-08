# Här ska alla todo:s finnas!
#imports 
import json
import os
# key = student_id, value = 
todos = {}

# prioritys 0-5 with 5 as most urgent!
# ############################
# todo = [(0, "Clean my room"),
#         (3, "Eat Pizza"),
#         (0, "Exercise")]

# ############################



def add_todo(student_id, priority, todo):
    """
    student_id: int

    priority: int
    
    todo: str

    ret --> None
    """
    # Kom ihåg att vi kanske får en ny student!
    # Kontrollera priority är mellan 0 och 5
    if priority <0 or priority >5:
        return None
    if student_id not in todos:
        todos[student_id] = []
    todos[student_id].append([priority, todo])

    

def get_most_urgent(student_id):
    """
    student_id: int

    ret --> str eller None
    """
    # Vi letar efter todos med högsta prioritet, vi tar första med högsta värde!

    if student_id not in todos or not todos[student_id]:
        return None
    
    #priority max
    for urgent in todos[student_id]:
        if urgent == max(todos[student_id]):
            most_urgent = urgent[1]
    return most_urgent


def get_first_todo(student_id):
    """
    student_id: int

    ret --> str eller None
    """
    # Returnerar första todo i listan 
    if student_id not in todos:
        return None   
    return str(todos[student_id][0][1])

def delete_todo(student_id, todo):
    """
    student_id: int

    todo: str

    ret --> bool
    """    
    # Kom ihåg att vi måste hitta vår todo först innan vi kan ta bort den!
    if student_id not in todos:
        return None
    
    for todo_item in todos[student_id]:
        if todo_item[1] == todo:
            todos[student_id].remove(todo_item)
            return True
        
    return False

def get_all_todos_string(student_id):
    """
    student_id: int

    ret --> str
    """     
    # Här ska vi konstruera en sträng som innehåller alla todos
    # Tänk på att det ska vara snyggt formaterat det vi skickar tillbaka:
    # 0 -> Städa rummet
    # 2 -> Ringa mormor
    # 1 -> Gå ut med hund
    if student_id not in todos:
        return None
    todos_string = ""
    for todo_item in todos[student_id]:
        todos_string = todos_string + str(todo_item[0]) + " -> " + str(todo_item[1]) + "\n"
    return todos_string

def save_todos():
    """
    ret --> None
    """
    # Här ska vi spara dictionary med todos till fil
    if todos == {}:
        return None
    else:
        with open("todos.json", "w") as f:
            json.dump(todos, f)
        print("Todos saved")

def read_todos():
    """
    ret --> None
    """
    # Här ska vi läsa in sparade todos och spara i vår dictionary "todos"
    global todos
    if not os.path.exists("todos.json"):
        return None
    else:
        with open("todos.json", "r") as f:
            todos = json.load(f)
            #convert to dict into int using pop
            for key in list(todos.keys()):
                todos[int(key)] = todos.pop(key)
            print("Todos loaded")

def main():
    print("Todo Menu")
    while True:
        print("\n1. Add todo")
        print("2. Get most urgent todo")
        print("3. Get first todo")
        print("4. Delete todo")
        print("5. Get all todos")
        print("6. Save")
        print("7. Load")
        print("0. Exit")

        choice = input("Choose: ")
        
        if choice == "1":
            student_id = input("Student ID: ")
            student_id = int(student_id)
            priority = input("Priority: ")
            priority = int(priority)
            todo = input("Todo: ")
            add_todo(student_id, priority, todo)
        elif choice == "2":
             student_id = input("Student ID: ")
             student_id = int(student_id)
             print(get_most_urgent(student_id))
        elif choice == "3":
            student_id = input("Student ID: ")
            student_id = int(student_id)
            print(get_first_todo(student_id))
        elif choice == "4":
            student_id = input("Student ID: ")
            student_id = int(student_id)
            todo = input("Todo: ")
            print(delete_todo(student_id, todo))
            print(get_all_todos_string(student_id))
        elif choice == "5":
            student_id = input("Student ID: ")
            student_id = int(student_id)
            print(get_all_todos_string(student_id))
        elif choice == "6":
            save_todos()
        elif choice == "7":
            read_todos()
        elif choice == "0":
            break
        else: 
            print("Choice invalid.")



###########################################
# Till den som implementerar funktionerna #
###########################################
if __name__ == "__main__":
    # Här i skriver ni all kod för att testköra funktionerna ni skapar!
    main()