#Daniele Taccini


#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
    #Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

#questa variabile contiene il nome
name: str = "Erik"

#questa variabile contiene il messaggio
message: str = f"Hello {name}, ti va di imparare python isieme?"

#stampa il messaggio
print(message)



#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

#rende nome tutto in maiuscolo
name_upper: str = name.upper()
#rende nome tutto in minuscolo
name_lower: str = name.lower()
#rende la primalettera di nome in maiuscolo
name_title: str = name.title()


print(f"\n{name_upper} ")
print(name_lower)
print(name_title)



#2-5. Famous Quote: Find a quote from a famous person you admire. 
    #Print the quote and the name of its author. Your output should look something like the following, 
    #including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”

#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. 
    #Then compose your message and represent it with a new variable called message. Print your message. 

#variabile contenente il nome dell'autore
author_name: str = "a"

#variabile contenente la citazione dell'autore
quote: str = "b"


#contiene il messaggio
message1: str = f"{author_name} una volta disse, \"{quote}.\""



#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
    #Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, 
    #like some file browsers do.

#variabile con nome del file e la sua estensione
file_name: str = "python_notes.txt"

#variabile con all'interno una funzione che leva l'estensione dal nome
file_name_noext: str = file_name.removesuffix(".txt")

#stampa il nome del file senza l'estensione
print(file_name_noext)



#3-1. Names: Store the names of a few of your friends in a list called names. 
    #Print each person’s name by accessing each element in the list, one at a time.


#creazione della lista di nomi
name_list: list = ["Daniele","Andrea","Alessandro","Francesco"]


#stampa i nomi nella lista uno per volta tramite 'for'
for i in name_list:

    print(i)



#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
    #The text of each message should be the same, but each message should be personalized with the person’s name.

#stampa per ogni nome della lista "ciao, 'name'"
for i in name_list:

    print(f"\nCiao, {i}")



#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
    #Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

#creazione lista di veicoli
list_vehicles: str = ["auto1","auto2","auto3","auto4"]

#ciclo per scrivere un messaggio per ogni variabile presente
for i in list_vehicles:

    print(f"\nmi piacerebbe avere {i}")



#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
    #Make a list that includes at least three people you’d like to invite to dinner. 
    #Then use your list to print a message to each person, inviting them to dinner.

#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
    #You’ll have to think of someone else to invite.
    # Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
    # Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
    # Print a second set of invitation messages, one for each person who is still in your list.

#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
    # Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
    # Use insert() to add one new guest to the beginning of your list.
    # Use insert() to add one new guest to the middle of your list.
    # Use append() to add one new guest to the end of your list.
    # Print a new set of invitation messages, one for each person in your list.

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
    # Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
    # Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, 
    #print a message to that person letting them know you’re sorry you can’t invite them to dinner.
    # Print a message to each of the two people still on your list, letting them know they’re still invited.
    # Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.


def manda_inviti(list_invited: list):

    #ciclo per scrivere l'invito per ogni nome presente nella lista
    for i in list_invited:

        print(f"\nCiao {i}, mi piacerebbe invitarti a cena.")

    

def ritira_inviti(list_invited: list):

    i: int = (len(list_invited))-1

    while(len(list_invited) > 2):

        print(f"\n{list_invited[i]}, sono dispiaciuto di dover annulare la cena organizata")
        list_invited.pop(i)
        i = (len(list_invited))-1

    print("\n")
    for j in list_invited:

        print(f"\n{j}, sei ancora invitato alla cena organizzata")

    del list_invited


    


#creazione lista invitati
list_invited: list = ["persona1","persona2","persona3","persona4"]

#chiamo la funzione che ho creato per mandare gli inviti
manda_inviti(list_invited)

print(f"\n\n{list_invited[2]} non potrà partecipare alla cena\n\n")

#sostituisco l'invitato che non può venire con una nuova persona
list_invited[2] = "persona5"

#richiamo la funzione che ho creato per mandare gli inviti
manda_inviti(list_invited)

print("\n\nCiao invitati, vi scrivo per informarvi di aver trovato un tavolo più grande")

#serve a trovare il centro della lista per inserire un nuovo invitato
middle = (len(list_invited))//2
list_invited.insert(middle,"persona7")
list_invited.insert(0,"persona0")
list_invited.append("persona6")

#richiamo la funzione che ho creato per mandare gli inviti
manda_inviti(list_invited)

print("\n\n\n")
ritira_inviti(list_invited)

print(f"\n{list_invited}")



#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
    # Store the locations in a list. Make sure the list is not in alphabetical order.
place: list = ["Tenerife","Florida","Giappone","Islanda","Marocco"]

# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
print(f"{place}")

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(f"{sorted(place)}")

# Show that your list is still in its original order by printing it.
print(f"{place}")

# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
print(f"{sorted(place, reverse=True)}")

# Show that your list is still in its original order by printing it again.
print(f"{place}")

# Use reverse()  to change the order of your list. Print the list to show that its order has changed.
place.reverse()
print(f"{place}")

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
place.reverse()
print(f"{place}")

# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
place.sort()
print(f"{place}")
# Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.
place.sort(reverse=True)
print(f"{place}")


#3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.

#print(f"sto invitando a cena {len(list_invited)} persone")


#3-10. Every Function: Think of things you could store in a list. 
    #For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like.
    #Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

lingue: list=["Ita","Ing","Fra","Giap","Spa","Chi"]

#inserisco all'inizio
lingue.insert(0,"Tedesco")
#inserisco alla fine
lingue.append("Por")

#rimuovo il suffisso della lingua in posizione zero(Tedesco) e la riinserisco dentro la lista
lingue[0] = lingue[0].removesuffix("esco")

i: int = 0

for z in lingue:

    #rende nome tutto in minuscolo
    lingue[i] = z.lower()
    #rende la primalettera di nome in maiuscolo
    lingue[i] = z.title()
    #rende nome tutto in maiuscolo
    lingue[i] = z.upper()

    i += 1

#ordino la lista in ordine alfabetico
lingue = sorted(lingue)
#inverto l'ordine della lista
lingue.reverse()

print(lingue)



#6-1. Person: Use a dictionary to store information about a person you know. 
    #Store their first name, last name, age, and the city in which they live. 
    #You should have keys such as first_name, last_name, age, and city. 
    #Print each piece of information stored in your dictionary.

#6-7. People: Start with the program you wrote for Exercise 6-1. 
    #Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. 
    #As you loop through the list, print everything you know about each person.
print("\n\n\n")
persona1: dict = {"first_name": "Mario", "last_name": "Rossi", "age": "40", "city": "Milano"}


for key in persona1:

    print(persona1[key])



#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
    #Think of five names, and use them as keys in your dictionary. 
    #Think of a favorite number for each person, and store each as a value in your dictionary. 
    #Print each person’s name and their favorite number.
print("\n\n\n")
lucky_number: dict = {"Mario": "5", "Francesco": "4", "Alessandro": "7", "Giulia": "8"}

for key in lucky_number:

    print(f"{key}: {lucky_number[key]}")


#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
    #Think of five programming words you’ve learned about in the previous chapters. 
    #Use these words as the keys in your glossary, and store their meanings as values.
    #Print each word and its meaning as neatly formatted output.
    #You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
    #Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
print("\n\n\n")
glossario: dict = {

    "Collections":
    "In Python, collections are data structures used to store and manipulate groups of related data.",

    "Control Statements":
    "Control statements in Python are constructs that alter the flow of program execution based on certain conditions or criteria.",

    "Loops":
    "Loops are programming structures that allow you to repeat a block of code multiple times. \nThey are essential for automating repetitive tasks and iterating over data.",

    "Functions":
    "Functions in programming are named blocks of code that perform a specific task. \nThey allow you to break down your code into smaller, reusable parts.",
}

for key in glossario:

    print(f"{key}:")

    print(f"{glossario[key]}\n")


#6-7. People: Start with the program you wrote for Exercise 6-1. 
    #Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. 
    #As you loop through the list, print everything you know about each person.
print("\n\n\n")
persona1: dict = {"first_name": "Mario", "last_name": "Rossi", "age": "40", "city": "Milano"}
persona2: dict = {"first_name": "Esposito", "last_name": "Bianchi", "age": "80", "city": "Napoli"}
persona3: dict = {"first_name": "Giulia", "last_name": "Verdi", "age": "20", "city": "Roma"}

people: list = [persona1, persona2, persona3]

for i in people:
    print("\n")
    for key in persona1:

        print(f"{key}: {i[key]}")



#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. 
    #In each dictionary, include the kind of animal and the owner’s name. 
    #Store these dictionaries in a list called pets. 
    #Next, loop through your list and as you do, print everything you know about each pet. 
print("\n\n\n")
pet1: dict = {"breed": "dog", "owner": "Esposito"}
pet2: dict = {"breed": "cat", "owner": "Mario"}
pet3: dict = {"breed": "rabbit", "owner": "Giulia"}


pet: list = [pet1, pet2, pet3]

for i in pet:

    print(i)



#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
    #Loop through the dictionary, and print each person’s name and their favorite places.
print("\n\n\n")
favorite_places: dict = {
    "Francesco": "La grande barriera corallina, Colosseo, Grande Muraglia cinese", 
    "Alessandro": "Taj Mahal, Grand Canyon, Templi di Angkor", 
    "Giulia": "Cascate di Iguazú, Machu Picchu, Golden Circle Route"}

for key in favorite_places:

     print(f"{key}: {favorite_places[key]}\n")



#6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
    #Then print each person’s name along with their favorite numbers.
print("\n\n\n")
more_lucky_number: dict = {"Mario": "5, 63", "Francesco": "4, 52", "Alessandro": "7, 92", "Giulia": "8, 37"}

for key in more_lucky_number:

    print(f"{key}: {more_lucky_number[key]}")


#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
    #Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. 
    #The keys for each city’s dictionary should be something like country, population, and fact. 
    #Print the name of each city and all of the information you have stored about it.
print("\n")
about_roma: dict = {"country": "Italia", "population": "2,8 milioni di persone", 
                    "fact": "Uno dei monumenti più famosi e visitati di Roma è il Colosseo. Questo antico anfiteatro, chiamato anche Anfiteatro Flavio, è stato il luogo di terribili battaglie tra gladiatori e animali, ma anche di spettacoli teatrali e di battaglie navali simulate."}

about_parigi: dict = {"country": "Francia", "population": "11,3 milioni di persone", 
                      "fact": "Parigi, la Ville Lumière, è indiscutibilmente famosa per le sue attrazioni iconiche come la Tour Eiffel o il Notre Dame, per i suoi musei di fama mondiale come il Louvre e l'Orsay e per essere considerata per antonomasia la città più romantica al mondo."}

about_Barcellona: dict = {"country": "Spagna", "population": "5,7 milioni di persone", 
                          "fact": "La Sagrada Familia è l’opera più famosa dell’architetto catalano Gaudí, che ha plasmato il paesaggio architettonico di Barcellona fino alla sua morte nel 1926."}

cities: dict = {"Roma": about_roma, "Parigi": about_parigi, "Barcellona": about_Barcellona}

for key in cities:

    print(f"\n\n{key.upper()}\n")

    for key1 in cities[key]:

        
        print(f"{key1}: {cities[key][key1]}")



#6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. 
    #Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.

print("\n\n")
#Extensions of 6-8
print("\n\n\n")
pet1: dict = {"Specie": "Cane", "Sesso": "Maschio", "Nome": "Rex", "Età": "7 anni", "Colore": "Nero", "Padrone": "Esposito"}
pet2: dict = {"Specie": "Gatto", "Sesso": "Femmina","Nome": "Simba", "Età": "12 anni", "Colore": "Rosso", "Padrone": "Mario"}
pet3: dict = {"Specie": "Coniglio", "Sesso": "Femmina","Nome": "Zucchero", "Età": "3 anni", "Colore": "Bianco", "Padrone": "Giulia"}
pet4: dict = {"Specie": "Uccello", "Sesso": "Maschio","Nome": "coco", "Età": "2 anni", "Colore": "Verde", "Padrone": "Carlo"}
pet5: dict = {"Specie": "Cavallo", "Sesso": "Maschio","Nome": "spirit", "Età": "20 anni", "Colore": "Marrone", "Padrone": "Alice"}



pet: list = [pet1, pet2, pet3, pet4, pet5]

for i in pet:
    print("\n")
    for key in pet1:

        print(f"{key}: {i[key]}")

     