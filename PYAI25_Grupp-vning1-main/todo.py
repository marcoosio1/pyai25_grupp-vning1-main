# Här ska alla todo:s finnas!
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
    pass

def get_most_urgent(student_id):
    """
    student_id: int

    ret --> str eller None
    """
    # Vi letar efter todos med högsta prioritet, vi tar första med högsta värde!
    pass

def get_first_todo(student_id):
    """
    student_id: int

    ret --> str eller None
    """
    # Returnerar första todo i listan    
    pass

def delete_todo(student_id, todo):
    """
    student_id: int

    todo: str

    ret --> bool
    """    
    # Kom ihåg att vi måste hitta vår todo först innan vi kan ta bort den!
    pass

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
    pass

def save_todos():
    """
    ret --> None
    """
    # Här ska vi spara dictionary med todos till fil

def read_todos():
    """
    ret --> None
    """
    # Här ska vi läsa in sparade todos och spara i vår dictionary "todos"


###########################################
# Till den som implementerar funktionerna #
###########################################
if __name__ == "__main__":
    # Här i skriver ni all kod för att testköra funktionerna ni skapar!
    pass