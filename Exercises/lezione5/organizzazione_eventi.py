#4. Event Organizer:

"""Write a function called plan_event() that accepts an event name, a list of participants, and an hour. 
    The function should return a dictionary that includes the event name and a list of the participants. 
    Call this function with varying numbers of participants to plan different events.
    Example: plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)
    Write a function called modify_event() that accepts a dictionary, an event name, and new details to modify an already planned event.
    Example: modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)"""

def plan_event(event: str, partecipanti: list, ora: str)->dict:

    dictionary: dict = {
        "Nome evento": event,
        "Partecipanti": partecipanti,
        "Orario": ora}

    return dictionary

def modify_event(dictionary: dict, event: str, partecipanti: list, ora: str)->dict:

    dictionary.update({"Partecipanti": partecipanti})
    dictionary.update({"Orario": ora})
    return dictionary

dictionary: dict = plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],"4pm")
print(dictionary)

dictionary = modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie","Francesco","Marco"], "6pm")
print(dictionary)