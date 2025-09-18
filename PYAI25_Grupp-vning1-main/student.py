# Här ska alla studenter finnas! 
# key = student id, value = dictionary student [se nedan]
students = {}

##########################
# student = {
#     "id": 1,
#     "name": "Jon",
#     "age": 23,
#     "courses": []
# }
##########################


def create_new_student(id,name,age):
    """
    student_id: int

    name: str

    age: int

    ret --> bool
    """
    # Vi ska skapa en ny student-dictionary med följande värden från våra parametrar!
    # Tänk på att vi inte kan skapa en student med samma id som någon annan!
    # Den som använder funktionen måste få veta om vi kunnat skapa en student eller inte!
    pass

def add_course(student_id, course):
    """
    student_id: int

    course: str

    ret --> int

    0 = ok

    1 = student_id saknas
    
    2 = kursen finns redan
    """
    # Här ska vi lägga till en kurs till listan om studenten existerar
    pass

def remove_course(student_id, course):
    """
    student_id: int

    course: str

    ret --> int

    0 = ok

    1 = student_id saknas

    2 = kursen finns inte
    """
    # Här tar vi bort en kurs om den existerar!
    pass

def get_student_name(student_id):
    """
    student_id: int

    ret --> namnet eller None
    """
    # givet korrekt student_id så returnerar vi namnet
    pass

def get_student_age(student_id):
    """
    student_id: int

    ret --> age eller None
    """
    # givet korrekt student_id så returnerar vi åldern
    pass

def get_student_courses(student_id):
    """
    student_id: int

    ret --> [courses] eller None
    """
    # givet korrekt student_id så returnerar vi en kopia av listan med kurser!
    pass

def save_students():
    """
    ret --> None
    """
    # Här ska vi spara dictionary med stundeter till fil

def read_students():
    """
    ret --> None
    """
    # Här ska vi läsa in sparade studenter och spara i vår dictionary "students"

###########################################
# Till den som implementerar funktionerna #
###########################################
if __name__ == "__main__":
    # Här i skriver ni all kod för att testköra funktionerna ni skapar!
    pass