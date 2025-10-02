# Här kommer alla events att sparas
import json
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
    for event in events:
        if event["event_name"] == event_name:
            return False  # event name already taken
    
    new_event = {
        "owner": student_id,
        "password": password,
        "event_name": event_name,
        "participants": [],
        "location": None
    }
    events.append(new_event)
    return True

def add_participants_to_event(student_id,event_name,password, participant):
    # Här lägger vi till en participant till önskat event
    """
    student_id: int
    event_name: str
    password: str
    participant: int

    ret --> bool
    """
    for event in events:
        if event["event_name"] == event_name and event["owner"] == student_id and event["password"] == password:
            if participant not in event["participants"]:
                event["participants"].append(participant)
                return True
            return False  # already added
    return False

def get_event(student_id,event_name,password):
    """
    student_id: int
    event_name: str
    password: str

    ret --> dict
    """
    # Här hämtar vi och returnerar ett event om det existerar
    for event in events:
        if event["event_name"] == event_name and event["owner"] == student_id and event["password"] == password:
            return event
    return None

def get_participants(student_id,event_name,password):
    """
    student_id: int
    event_name: str
    password: str

    ret --> lista med int eller tom lista eller None
    """
    # Här hämtar vi participats till ett event om det existerar
    event = get_event(student_id, event_name, password)
    if event:
        return event["participants"]
    return []


def save_events():
    """
    ret --> None
    """
    # Här ska vi spara listan med events till fil
with open("events.json", "w", encoding="utf-8") as f:
        json.dump(events, f)
def read_events():
    """
    ret --> None
    """
    # Här ska vi läsa in sparade events och spara i vår lista "events"

    global events
    try:
        with open("events.json", "r", encoding="utf-8") as f:
            events = json.load(f)
    except FileNotFoundError:
        events = []
###########################################
# Till den som implementerar funktionerna #
###########################################
if __name__ == "__main__":
    # Här i skriver ni all kod för att testköra funktionerna ni skapar!
    read_events()

    print("Skapar event...")
    print(create_event(1, "Studentfest", "hemligt"))  # True
    print(create_event(1, "Studentfest", "hemligt"))  # False 

    print("\nLägger till deltagare...")
    print(add_participants_to_event(1, "Studentfest", "hemligt", 2))  # True
    print(add_participants_to_event(1, "Studentfest", "hemligt", 2))  # False

    print("\nHämta event:")
    print(get_event(1, "Studentfest", "hemligt"))

    print("\nHämta deltagare:")
    print(get_participants(1, "Studentfest", "hemligt"))

    save_events()