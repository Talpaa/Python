class RecipeManager:

    def __init__(self) -> None:
        
        self.ricettario: dict[str, list[str]] = {}

    def create_recipe(self, name: str, ingredients: list [str]):

        #name = name.title()
        
        if name not in self.ricettario:

            ricettario: dict[str, list[str]] = {}


            self.ricettario[name] = ingredients
            return self.ricettario

        else:

            return f'Errore: Ricetta già esistente'
        

    def add_ingredient(self, recipe_name: str, ingredient: str):

        #recipe_name = recipe_name.title()
        #ingredient = ingredient.title()
        message: str = '{'

        if recipe_name in self.ricettario:
            
            for ingredient_in_list in self.ricettario[recipe_name]:

                if ingredient_in_list == ingredient:

                    return f'Errore: Ingrediente già presente nella ricetta'

            
            self.ricettario[recipe_name].append(ingredient)
            message += f'\'{recipe_name}\': {self.ricettario[recipe_name]}'
            message += '}'

            return message


        else:

            return f'Errore: Ricetta inesistente'
        
    
    def remove_ingredient(self, recipe_name: str, ingredient: str):

        #recipe_name = recipe_name.title()
        #ingredient = ingredient.title()
        controllo: bool = False

        if recipe_name in self.ricettario:
            
            for ingredient_in_list in self.ricettario[recipe_name]:

                if ingredient_in_list == ingredient:

                    controllo = True
                
            if controllo:
                message: str = '{\''
                self.ricettario[recipe_name].remove(ingredient)
                message += f'{recipe_name}\': {self.ricettario[recipe_name]}'
                message += '}'
                return message

            else:
                
                return f'Errore: Ingrediente non presente nella ricetta'
            
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):

        #recipe_name = recipe_name.title()
        #old_ingredient = old_ingredient.title()
        #new_ingredient = new_ingredient.title()

        message: str = '{'

        controllo: bool = False

        if recipe_name in self.ricettario:
            
            for ingredient_in_list in self.ricettario[recipe_name]:

                if ingredient_in_list == old_ingredient:

                    controllo = True
                
            if controllo:

                index: int = self.ricettario[recipe_name].index(old_ingredient)
                self.ricettario[recipe_name].remove(old_ingredient)
                self.ricettario[recipe_name].insert(index, new_ingredient)

                message += f'\'{recipe_name}\': {self.ricettario[recipe_name]}'
                message += '}'

                return message

            else:
                
                return f'Errore: Ingrediente non presente nella ricetta'
            
    def list_recipes(self):

        message: str = ''

        for ricetta in self.ricettario:

            message += f'[\'{ricetta}\']' 

        
        if len(self.ricettario) > 0:

            return message
        
        else:

            return f'Errore: non sono presenti ricette nel ricettario'
        
    def list_ingredients(self, recipe_name: str): 

        #recipe_name = recipe_name.title()

        if recipe_name in self.ricettario:

            message: str = f'{self.ricettario[recipe_name]}'

        else:

            return f'Errore: ricetta non presente nel ricettario'
        
        return message

    def search_recipe_by_ingredient(self, ingredient: str):

        message: str = '{'
        flag: bool = False

        for ricetta in self.ricettario:

            if ingredient in self.ricettario[ricetta]:
                
                flag = True
                message += f'\'{ricetta}\': {self.ricettario[ricetta]}'
                message += '}'
        if flag:

            return message
        
        else:

            return f'Errore: nessuna ricetta presente nel ricettario non usa l\'ingrediente \'{ingredient}\''
        

print()
print()
print()
	
manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))