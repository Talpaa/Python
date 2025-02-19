class Food:

    # - nome
    # - prezzo
    # - descrizione

    def __init__(self, name: str, price: float, description: str = None) -> None:
        
        self.name = name
        self.price = price
        self.description = description

    def __str__(self) -> str:
        
        return f"{self.name}: prezzo {self.price}$"

class Menu:

    # - lista di cibo

    def __init__(self, foods: list[Food] = []):
        
        self.foods: list[Food] = foods

    def add_food(self, foods: Food):
        
        self.foods.append(foods)
    
    def remove_food(self, foods: Food):
        
        if foods in self.foods:

            self.foods.remove(foods)

    def __str__(self) -> str:
        
        repr: str = ""

        for food in self.foods:

            repr += "\n" + str(food)

        return repr[1:]

menu = Menu()

menu.add_food(Food("Hamburger", 5.00, "Hamburger di scottona da 250gr"))
menu.add_food(Food("patatine fritte",3.50,"Porzione di patatine fritte con buccia da 150gr"))
menu.add_food(Food("Bottiglia d'acqua",1.50,"bottiglia d'acqua da 0,75 l"))

print(menu)