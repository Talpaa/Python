#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
    # Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. 
    #For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
    # Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
    #The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
print("\n\n\n")
pizza: list = ["Margherita", "Diavola", "Crostino"]

for i in pizza:

    print(f"Mi piace molto come pizza il gusto {i}\n")

print("Mi piace molto la pizza")

#4-2. Animals: Think of at least three different animals that have a common characteristic. 
    #Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
    # Modify your program to print a statement about each animal, such as A dog would make a great pet.
    # Add a line at the end of your program, stating what these animals have in common. 
    #You could print a sentence, such as Any of these animals would make a great pet!
print("\n\n\n")
animali: list = ["Cane", "Gatto", "Coniglio"]

for i in animali:

    print(f"Mi piace molto il {i} come animale\n")

print("Tutti questi animali hanno la coda")

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
print("\n\n\n")

for i in range(1,21):

    print(f"{i}")

#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
    #(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
numeri: list = []
for i in range(1,1000001):

    numeri.append(i)

for i in numeri:

    #print(i)
    break
#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. 
    #Also, use the sum() function to see how quickly Python can add a million numbers.
print("\n\n\n")
print(f"Il numero più piccolo nella lista è {min(numeri)}")

print(f"Il numero più grande nella lista è {max(numeri)}")

print(f"La somma di tutti i numeri della lista è {sum(numeri)}")

#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
print("\n\n\n")
odd_numbers: list = []

for i in range(1,20,2):

    odd_numbers.append(i)

for i in odd_numbers:

    print(f"{i}")

#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
print("\n\n\n")
threes: list = []

for i in range(3,31,3):

    threes.append(i)

for i in threes:

    print(f"{i}")
#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
    #Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.ù
print("\n\n\n")
cubes: list = []

for i in range(1,11):

    cubes.append(i**3)

for i in cubes:
    print(i)

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
print("\n\n\n")
cubes_comprehension: list = [i**3 for i in range(1,11)]

for i in cubes_comprehension:
    print(i)

#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
    # Print the message The first three items in the list are:. 
    #Then use a slice to print the first three items from that program’s list.
    # Print the message Three items from the middle of the list are:. 
    #Then use a slice to print three items from the middle of the list.
    # Print the message The last three items in the list are:. 
    #Then use a slice to print the last three items in the list.
print(f"I primi tre cubi nella lista sono: {cubes_comprehension[slice(3)]}")

print(f"I tre cubi in mezzo alla lista sono: {cubes_comprehension[slice(3,6)]}")

print(f"Gli ultimi tre cubi nella lista sono: {cubes_comprehension[slice(len(cubes_comprehension),(len(cubes_comprehension)-4),-1)]}")

#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
    # Add a new pizza to the original list.
    # Add a different pizza to the list friend_pizzas.
    # Prove that you have two separate lists. 
    #Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
    #Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
    #Make sure each new pizza is stored in the appropriate list.
print("\n\n\n")
friend_pizza: list = ["Margherita", "Diavola", "Crostino"]

pizza.append("Napoli")
friend_pizza.append("Wurstel e patatine")

print(f"I miei gusti di pizza preferiti sono:")
for i in pizza:
    print(i)
print("\n")
print(f"I gusti di pizza preferiti del mio amico sono:")
for i in friend_pizza:
    print(i)

#4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.

#4-1
print("\n\n\n")

pizza = ["Margherita", "Diavola", "Crostino"]

for i in pizza:
    print(f"Mi piace molto come pizza il gusto {i}\n")

print("Mi piace molto la pizza")

#4-2
print("\n\n\n")

animali = ["Cane", "Gatto", "Coniglio"]

for i in animali:
    print(f"Mi piace molto il {i} come animale\n")

print("Tutti questi animali hanno la coda")

#4-3
print("\n\n\n")

for i in range(1, 21):
    print(f"{i}")


#5-1. Conditional Tests: Write a series of conditional tests. 
    #Print a statement describing each test and your prediction for the results of each test. 
    #Your code should look something like this: car = 'subaru'
    #print("Is car == 'subaru'? I predict True.")
    #print(car == 'subaru')
    #print("\nIs car == 'audi'? I predict False.")
    #print(car == 'audi')
    # Look closely at your results, and make sure you understand why each line evaluates to True or False.
    # Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

#5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10.     
    #If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
    #Have at least one True and one False result for each of the following:
    # Tests for equality and inequality with strings
    # Tests using the lower() method
    # Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to.
    # Tests using the and keyword and the or keyword
    # Test whether an item is in a list
    # Test whether an item is not in a list
print("\n\n\n")
car: list = ['Subaru', 'Audi', ]
print("La macchina scelta è una Subaru? Secondo me uscira 'True'.")
print(car[0].lower() == 'subaru')

print("La macchina scelta non è una Subaru? Secondo me uscira 'False'.")
print(car[0].lower() != 'subaru')

print("\nLa macchina scelta è un'Audi? Secondo me uscira 'False'.")
print(car[1].lower() == 'audi')

#test
print("\n")
print(car[0].lower() == car[1].lower())

print(car[0].lower() == 'SUBARU'.lower())

print(car[0] == car[1])
print(car[0] != car[1])
print(car[0] > car[1])
print(car[0] < car[1])
print(car[0] >= car[1])
print(car[0] <= car[1])

print((car[0] != car[1])and(car[0] > car[1]))
print((car[0] != car[1])or(car[0] < car[1]))

if 'Subaru' in car: print(f'Subaru è presente nel catalogo {True}')

if 'mercedes' not in car: print(f'Mercedes non è presente nel catalogo {True}')

#5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
    # Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
    # Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
print("\n\n\n")

alien_color: str = 'green'

if alien_color == 'green':

    print("Hai guadagnato 5 punti")

if alien_color == 'red':

    pass

#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
    # If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
    # If the alien’s color isn’t green, print a statement that the player just earned 10 points.
    # Write one version of this program that runs the if block and another that runs the else block.
print("\n")
alien_color = 'yellow'
if alien_color == 'green':

    print("Hai guadagnato 5 punti")

else:

    print("Hai guadagnato 10 punti")

#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
    # If the alien is green, print a message that the player earned 5 points.
    # If the alien is yellow, print a message that the player earned 10 points.
    # If the alien is red, print a message that the player earned 15 points.
    # Write three versions of this program, making sure each message is printed for the appropriate color alien.
print("\n")
alien_color = 'red'
if alien_color == 'green':

    print("Hai guadagnato 5 punti")
elif alien_color == 'yellow':

    print("Hai guadagnato 10 punti")
else:

    print("Hai guadagnato 15 punti")
#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
    # If the person is less than 2 years old, print a message that the person is a baby.
    # If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
    # If the person is at least 4 years old but less than 13, print a message that the person is a kid.
    # If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
    # If the person is at least 20 years old but less than 65, print a message that the person is an adult.
    # If the person is age 65 or older, print a message that the person is an elder.
print("\n\n\n")
age: int = 65

if age < 2:
    print("Sei un neonato")
elif age < 4:
    print("Sei un bambino")
elif age < 13:
    print("Sei un ragazzino")
elif age < 20:
    print("Sei un ragazzo")
elif age < 65:
    print("Sei un adulto")
else:
    print("Sei un anziano")

#5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
    # Make a list of your three favorite fruits and call it favorite_fruits.
    # Write five if statements. Each should check whether a certain kind of fruit is in your list. 
    #If the fruit is in your list, the if block should print a statement, such as You really like Apples!
print("\n\n\n")
fruit: list = ['pesca','mela','anguria']

if 'pesca' in fruit:
    print("Ti piacciono davvero le pesche")

if 'mela' in fruit:
    print("Ti piacciono davvero le mele")

if 'anguria' in fruit:
    print("Ti piacciono davvero le angurie")

if 'arancia' in fruit:
    print("Ti piacciono davvero le arance")

if 'uva' in fruit:
    print("Ti piacciono davvero l' uva")

#5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. 
    #Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
    # If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
    # Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
print("\n\n\n")
usernames: list = ["admin",'a','b','c','d']

for i in usernames:

    if i == 'admin':
        print("Ciao admin, ti piacerebbe vedere lo status report?")

    else:
        print(f"Ciao {i}, grazie per aver fatto di nuvo accesso al sito")

#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
    # If the list is empty, print the message We need to find some users!
    # Remove all of the usernames from your list, and make sure the correct message is printed.
print("\n")
usernames.clear()

if len(usernames) == 0: print("Dovremmo trovare alcuni utenti")

#5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
    # Make a list of five or more usernames called current_users.
    # Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
    # Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. 
    #If a username has not been used, print a message saying that the username is available.
    # Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
    #(To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
print("\n\n\n")
current_users: list = ['a','b','c','d','e']
new_users: list = ['a','f','g','d','h']
a: int = 0
for i in new_users:

    for j in current_users:

        if i.lower() == j.lower():
            print("Questo username non è disponibile")
            a += 1

    if a == 0:
        print("Questo username è disponibile")
    a = 0
#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
    # Store the numbers 1 through 9 in a list.
    # Loop through the list.
    # Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
    #Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
print("\n\n\n")
num: list = [1,2,3,4,5,6,7,8,9]

for c in num:

    if c == 1:

        print(f"{c}st")

    elif c == 2:

        print(f"{c}nd")

    elif c == 3:

        print(f"{c}rd")

    else:
        print(f"{c}th")
