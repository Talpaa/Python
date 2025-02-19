#8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. 
    #Call the function, and make sure the message displays correctly.
print("\n")
def display_message():

    print("Sto imparando un sacco di cose")

display_message()

#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
    #The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
    #Call the function, making sure to include a book title as an argument in the function call.
print("\n\n\n")
def favorite_book(book):
    print(f"Uno dei miei libri preferiti è {book}")

favorite_book("Alice in Wonderland")
#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
    #The function should print a sentence summarizing the size of the shirt and the message printed on it. 
    #Call the function once using positional arguments to make a shirt. 
    #Call the function a second time using keyword arguments.

#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
    #Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
print("\n\n\n")
def make_shirt(size: str,text: str):
     
    if (size.lower() == ('m')) or (size.lower() == ('l')):
     
        print(f"La taglia della maglietta è: {size}")
        print(f"Il testo che dovrà essere stampato sulla maglietta è:")
        print(f"I love Python\n")
    else:
        print(f"La taglia della maglietta è: {size}")
        print(f"Il testo che dovrà essere stampato sulla maglietta è:\n {text}\n")

make_shirt("M", None)

make_shirt(text = "b", size = "XL")


#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
    #The function should print a simple sentence, such as Reykjavik is in Iceland. 
    #Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.
print("\n\n\n")
def describe_city(city: str = "Roma", country: str = "Italia"):
    print(f"{city} è in {country}")

describe_city()
describe_city("Stoccolma","Svezia")
describe_city("New Delhi","India")
describe_city("Brasília","Brazil")
#8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
    #The function should return a string formatted like this: "Santiago, Chile". 
    #Call your function with at least three city-country pairs, and print the values that are returned.
print("\n\n\n")
def city_country(city: str, country: str)->str:
    frase: str = (f"{city}, {country}")

    return frase

frase: str = ""
frase = city_country("Roma","Italia")
print(frase)
frase = city_country("Stoccolma","Svezia")
print(frase)
frase = city_country("New Delhi","India")
print(frase)
frase = city_country("Brasília","Brazil")
print(frase)
#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
    #The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
    #Use the function to make three dictionaries representing different albums. 
    #Print each return value to show that the  dictionaries are storing the album information correctly. 
    #Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
    #If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
    #Make at least one new function call that includes the number of songs on an album.
print("\n\n\n")
def print_album(album: dict):
    
    for key in album:

        if album[key] != None:
            print(f"{key}: {album[key]}")

    print("\n")

def make_album(artist: str,album: str,num: str = None)->dict:
    
    info_album: dict ={"Artist": artist, "Album": album, "Canzoni": num}
    return info_album

print_album(make_album("Mace","Maya","16"))

print_album(make_album("Gemitaiz","QVC 10","22"))

print_album(make_album("Stabber","Trueno","11"))

print_album(make_album("Taxi B","ZOLFO"))
#8-8. User Albums: Start with your program 
    #from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
    #Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
    #Be sure to include a quit value in the while loop.
controllo: bool = True
n: str = "0"
while controllo == True:
    
    artista = input("Iserisci il nome dell'artista che ha creato l'album: ")

    titolo = input("Iserisci il nome dell'album: ")

    canzoni = input("Iserisci il numero di canzoni presenti nell'album: ")

    print("\n")
    print_album(make_album(artista,titolo,canzoni))
    print("\n")

    print("Iserisci 1(UNO) per creare un nuovo album")
    n = input("Iserisci 0(ZERO) per creare uscire dal programma: ")
    print("\n")

    if n != ("1"):

        controllo = False

#8-9. Messages: Make a list containing a series of short text messages. 
    #Pass the list to a function called show_messages(), which prints each text message.

#8-10. Sending Messages: Start with a copy of your program 
    #from Exercise #8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
    #After calling the function, print both of your lists to make sure the messages were moved correctly.

#8-11. Archived Messages: Start with your work from Exercise #8-10. Call the function send_messages() with a copy of the list of messages. 
    #After calling the function, print both of your lists to show that the original list has retained its messages.
print("\n\n\n")
def show_messages(lista: list):

    for i in lista:

        print(i)

def send_messages(lista: list)->list:

    messaggi_inviati = []

    for i in lista:

        messaggi_inviati.append(i)
        print(i)

    return messaggi_inviati

messaggi: list = ["Ciao, come stai?","bene e te?","bene, fai qualcosa stasera?","no, avevi in mente qualcosa?"]

show_messages(messaggi)
messaggi_inviati: list = send_messages(messaggi)

print(messaggi)
print(messaggi_inviati)

copia_messaggi = send_messages(messaggi)

print(messaggi)
print(copia_messaggi)




#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
    #The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. 
    #Call the function three times, using a different number of arguments each time.
print("\n\n\n")

def sandwiches(ingredienti: list,num: int)->int:
    
    n: int = 1

    print(f"Panino numero #{num}")
    print(f"INGREDIENTI:\n")

    for i in ingredienti:
        print(f"    {n}){i}")
        n += 1
    
    print("\n")
    num += 1
    return num
    

num: int = 1

panino1: list = ["pane","tonno","pomodori"]
num = sandwiches(panino1,num)

panino2: list = ["pane","insalata","gamberetti","maionese"]
num = sandwiches(panino2,num)

panino3: list = ["pane","prosciutto cotto", "formaggio"]
num = sandwiches(panino3,num)


#8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. 
    #All the values must be passed to the function as parameters.
    #The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
print("\n\n\n")
def build_profile(profilo: list)->str:
    
    stringa_profilo: str = f"{nome} {cognome}, {età} anni, capelli {capelli}, {peso} Kg"

    return stringa_profilo

nome: str = "Eric"
cognome: str = "Crow"
età: str = "45"
capelli: str = "marroni"
peso: str = "67"

profilo: list = [nome, cognome, età, capelli, peso]

stringa_profilo: str = build_profile(profilo)

print(stringa_profilo)

#8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. 
    #It should then accept an arbitrary number of keyword arguments. 
    #Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
    #Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
    #Print the dictionary that’s returned to make sure all the information was stored correctly. 
print("\n\n\n")
def make_car(casa_produttrice: str,modello: str,colore: str, traino: bool)->dict:
    
    car: dict = {
        "Casa_produttrice": casa_produttrice,
        "modello": modello,
        "colore": colore,
        "traino": traino
        }
    
    return car

car = make_car('subaru', 'outback', colore='blu', traino=False)

for key in car:

    if car[key] == True:

        print(f"{key.upper()}: presente")

    elif car[key] == False:

        print(f"{key.upper()}: non presente")

    else:
        print(f"{key.upper()}: {car[key]}")

#8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
    #Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

#prof purtroppo credo che il file printing_models di cui parli l'esercizio 8-15 non è stao dato come esercizio

#8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. 
    #Import the function into your main program file, and call the function using each of these approaches:
    #import module_name
    #from module_name import function_name
    #from module_name import function_name as fn
    #import module_name as mn
    #from module_name import *
print("\n\n\n")
import module_name

from module_name import manda_inviti
from module_name import manda_inviti as fn

import module_name as mn

from module_name import *

#creazione lista invitati
list_invited: list = ["persona1","persona2","persona3","persona4"]

#chiamo la funzione che ho importato dal file module_name.py per mandare gli inviti
manda_inviti(list_invited)


#8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.

#8-11 in pep8

print("\n\n\n")

def show_messages(lista: list):
    for i in lista:
        print(i)

def send_messages(lista: list) -> list:
    messaggi_inviati = []
    for i in lista:
        messaggi_inviati.append(i)
        print(i)
    return messaggi_inviati

messaggi: list = ["Ciao, come stai?", "bene e te?", "bene, fai qualcosa stasera?", "no, avevi in mente qualcosa?"]

show_messages(messaggi)
messaggi_inviati: list = send_messages(messaggi)

print(messaggi)
print(messaggi_inviati)

copia_messaggi = send_messages(messaggi)

print(messaggi)
print(copia_messaggi)

#8-12 in pep8

print("\n\n\n")

def sandwiches(ingredienti: list, num: int) -> int:
    n: int = 1

    print(f"Panino numero #{num}")
    print(f"INGREDIENTI:\n")

    for i in ingredienti:
        print(f"    {n}){i}")
        n += 1
    
    print("\n")
    num += 1
    return num
    

num: int = 1

panino1: list = ["pane", "tonno", "pomodori"]
num = sandwiches(panino1, num)

panino2: list = ["pane", "insalata", "gamberetti", "maionese"]
num = sandwiches(panino2, num)

panino3: list = ["pane", "prosciutto cotto", "formaggio"]
num = sandwiches(panino3, num)


#8-13 in pep8
print("\n\n\n")

def build_profile(profilo: list) -> str:
    stringa_profilo: str = f"{profilo[0]} {profilo[1]}, {profilo[2]} anni, capelli {profilo[3]}, {profilo[4]} Kg"
    return stringa_profilo

nome: str = "Eric"
cognome: str = "Crow"
età: str = "45"
capelli: str = "marroni"
peso: str = "67"

profilo: list = [nome, cognome, età, capelli, peso]

stringa_profilo: str = build_profile(profilo)

print(stringa_profilo)
