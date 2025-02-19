#2. Book Collection:

"""Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. 
    This function should return a dictionary where the author's name is the key and the value is a list of their books. 
    Demonstrate this function by adding books for different authors.
    Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])
    Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details. 
    This function should return an updated dictionary.
    Example: delete_book(dictionary, “Mark Twain”)"""


def add_book(author: str,collezione: list)->dict:

    collezione = set(collezione)

    collezione = list(collezione)

    libreria: dict = {author: collezione}
    
    return libreria

def delete_book(libreria: dict, author: str)->dict:

    if author in libreria:

        del libreria[author]

    return libreria

        



libreria: dict = add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])
print(libreria)

libreria = delete_book(libreria, "Mark Twain")
print(libreria)
