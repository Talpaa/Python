#5. Shopping List:

"""Write a function called create_shopping_list() that accepts a store name and any number of items as arguments. 
    It should return a dictionary with the store name and a set of items to buy there. Test the function with different stores and item lists.
    Example: create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})
    Write a function called print_shopping_list() that accepts a dictionary and a store name, then prints each item from that store's shopping list.
    Example: print_shopping_list(dictionary, "Grocery Store")"""


def create_shopping_list(store: str, prodotti: list)->dict:

    prodotti = set(prodotti)

    prodotti = list(prodotti)

    dictionary: dict = {"Negozio": store, "Prodotti": prodotti}

    return dictionary

def print_shopping_list(dictionary: dict, store: str):

    count: int = 1
    print(f"{store.upper()}:")

    for i in dictionary["Prodotti"]:

        print(f"{count}){i}")
        count += 1


dictionary: dict = create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})

print_shopping_list(dictionary, "Grocery Store")