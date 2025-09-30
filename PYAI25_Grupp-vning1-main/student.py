import json

# Här ska alla studenter finnas! 
# key = student id, value = dictionary student [se nedan]

students = {}
course_list = ["math", "physics", "chemistry"]

##########################
# student = {
#     "id": 1,
#     "name": "Jon",
#     "age": 23,
#     "courses": []
# }
##########################

##############################################################################################################


def create_new_student1(student_id, name, age):

    if student_id in students:

        return False
    
    students[student_id] = {"id": student_id, "name": name, "age": age, "courses": []} # Läggs till i dict för students med nyckeln students_id

    return True
    
    # Vi ska skapa en ny student-dictionary med följande värden från våra parametrar!
    # Tänk på att vi inte kan skapa en student med samma id som någon annan!
    # Den som använder funktionen måste få veta om vi kunnat skapa en student eller inte!
    
##############################################################################################################


def add_course1(student_id, course):

    if student_id not in students:
        return 1
    
    if course in students[student_id]["courses"]:
        return 2
    
    if course not in course_list:
        return 3
    
    else:
        students[student_id]["courses"].append(course)
        return 0

    # Här ska vi lägga till en kurs till listan om studenten existerar
    
##############################################################################################################


def remove_course1(student_id, course):
    if student_id not in students:
        return 1
    
    if course not in students[student_id["courses"]] or (course not in course_list):
        return 2
    
    else:
        students[student_id]["courses"].remove(course)
        return 0

    # Här tar vi bort en kurs om den existerar!
    
##############################################################################################################


def get_student_name(student_id):

    if student_id in students:
        return students[student_id]["name"]
    else:
        return None

    # givet korrekt student_id så returnerar vi namnet

############################################################################################################## 


def get_student_age(student_id):

    if student_id in students:
        return students[student_id]["age"]
    else:
        return None

    # givet korrekt student_id så returnerar vi åldern
    
##############################################################################################################


def get_student_courses(student_id):

    if student_id in students:
        return students[student_id]["courses"]
    else:
        return None

    # givet korrekt student_id så returnerar vi en kopia av listan med kurser!

##############################################################################################################


def save_students():

    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(students, f, indent=1, ensure_ascii=False)

    # Här ska vi spara dictionary med stundeter till fil

##############################################################################################################


def read_students():

    global students

    try:
        with open("students.json", "r", encoding="utf-8") as f:
            students = json.load(f)

            students = {int(id): student_data for id, student_data in students.items()} 

            #Konverterar tillbaka id-nyckeln till int från str då json sparar allt som str.

    except FileNotFoundError:
        print("Ingen fil hittad.")
        students = {}

    # Här ska vi läsa in sparade studenter och spara i vår dictionary "students"

##############################################################################################################


def create_new_student():

    try:

        student_id = int(input("Student id: "))
        name = input("Student name: ")
        age = int(input("Student age: "))

        # Om funktionen returnerar true körs if-satsen, om den returnerar false körs else-satsen.

        if create_new_student1(student_id, name, age):
            print(f"Student {name} with id {student_id} was added.")
            save_students()
            input("Press enter to continue.")

        else:
            print("A student with that id already exists.")

    except ValueError: # Om nån input inte stämmer reagerar valuerror.
        print("Invalid registration, Name = text, id and age = digits.") 

############################################ Add course ############################################################


def add_course():    

    try:
        
        student_id = int(input("Student id: "))
        course = input("Course: ").lower()

        output = add_course1(student_id, course)

        # Här händer följande:

        # Funktionen add_course anropas med de två argumenten student_id och courses
        # Funktionen kör sin kod
        # Den kollar om student-id finns i students
        # Den kollar om kursen redan finns i studentens "courses"-lista
        # Den kollar ifall kursen finns i kurslistan.
        # Om allt är okej → kursen läggs till i listan
        # Sedan returnerar funktionen en statuskod (t.ex. 0, 1, 2, 3)
        # Returnvärdet sparas i variabeln output.
        # Om funktionen returnerar 0, så blir output = 0
        # Om den returnerar 1, så blir output = 1, osv.

        # Menyn använder output för att avgöra vilket meddelande som ska skrivas ut.

        if output == 0:
            print(f"{course} added for {get_student_name(student_id)}")
            save_students()
            input("Press enter to continue.")
            
        elif output == 1:
            print("Wrong id, student not registred.")

        elif output == 2:
            print("Course already added.")
        
        elif output == 3:
            print("Course not avalible.")

    except ValueError:
        print("Invalid registration, id = digits, courses = text.")

############################################ Remove course ############################################################


def remove_course():

    try:

        student_id = int(input("Student id: "))
        course = input("Course to remove: ")

        output = remove_course1(student_id, course)

        if output == 0:
            print(f"{course} removed from student {get_student_name(student_id)}")
            save_students()
            input("Press enter to continue.")

        elif output == 1:
            print("Wrong id, student not registred.")

        elif output == 2:
            print("Course not registred with student.")

    except ValueError:
        print("Invalid registration, id = digits, courses = text.")

############################################ Show a student ############################################################


def show_student():

    try:

        student_id = int(input("Student id: "))

        if student_id in students:
            
            print(f"id: {student_id}")
            print(f"Name: {get_student_name(student_id)}")
            print(f"Age: {get_student_age(student_id)}")
            if students[student_id]["courses"]:
                print(f"Courses: {', '.join(get_student_courses(student_id))}") # .join lägger ihop raderna i loopen efter varandra separerat med det skrivet framför .join
            else:
                print("No courses registred.")
            input("Press enter to continue.")
        else:
            print("Student not registred.")

    except ValueError:
        print("Invalid input, only digits in id-number")

############################################ Show all students ############################################################


def show_all_students():

    print("~" * 30)

    for student_id in students:
            print(f"id: {student_id}")
            print(f"Name: {get_student_name(student_id)}")
            print(f"Age: {get_student_age(student_id)}")
            if students[student_id]["courses"]:
                print(f"Courses: {', '.join(get_student_courses(student_id))}") # .join lägger ihop raderna i loopen efter varandra separerat med det skrivet framför .join
            else:
                print("No courses registred.")
            print("~" * 30)
            input("Press enter to continue.")

########################################################################################################





