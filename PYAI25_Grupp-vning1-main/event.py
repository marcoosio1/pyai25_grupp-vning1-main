# Här kommer alla events att sparas
events = []

# ######################
# event = {
#     "owner": 23, # student_id
#     "password": "secret!",
#     "event_name": "Studentfest"
#     "participants": [1,34,55],
#     "location": "Västerås Slott"
# }
# ######################

def create_event(student_id,event_name,password):
    """
    student_id: int
    event_name: str
    password: str

    ret --> bool
    """
    # Här skapar vi ett nytt event och lägger till i listan
    pass

def add_participants_to_event(student_id,event_name,password, participant):
    # Här lägger vi till en participant till önskat event
    """
    student_id: int
    event_name: str
    password: str
    participant: int

    ret --> bool
    """
    pass

def get_event(student_id,event_name,password):
    """
    student_id: int
    event_name: str
    password: str

    ret --> dict
    """
    # Här hämtar vi och returnerar ett event om det existerar
    pass

def get_participants(student_id,event_name,password):
    """
    student_id: int
    event_name: str
    password: str

    ret --> lista med int eller tom lista eller None
    """
    # Här hämtar vi participats till ett event om det existerar
    pass


def save_events():
    """
    ret --> None
    """
    # Här ska vi spara listan med events till fil

def read_events():
    """
    ret --> None
    """
    # Här ska vi läsa in sparade events och spara i vår lista "events"


###########################################
# Till den som implementerar funktionerna #
###########################################
if __name__ == "__main__":
    # Här i skriver ni all kod för att testköra funktionerna ni skapar!
    pass