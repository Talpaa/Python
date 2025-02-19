class RecipeManager:

    def __init__(self) -> None:
        
        self.ricettario: dict[str:list[str]] = {}

    def create_recipe(self, name: str, ingredients: list[str])->str:

        if name in self.ricettario:

            return f'Errore: Ricetta già presente'
        
        self.ricettario[name] = ingredients

        dizio: dict[str:list[str]] = {name: ingredients}

        return f'{dizio}'

    def add_ingredient(self, recipe_name: str, ingredient: str)->str:

        if recipe_name in self.ricettario:

            if ingredient in self.ricettario[recipe_name]:

                return f'Errore: Questo ingrediente è gia presente in questa ricetta'

            else:

                self.ricettario[recipe_name].append(ingredient)

                dizio: dict[str:list[str]] = {recipe_name: self.ricettario[recipe_name]}

                return f"{dizio}"
                
        else:

            return f'Errore: Questa ricetta non esiste'
        
    def remove_ingredient(self, recipe_name: str, ingredient: str)->str:

        if recipe_name in self.ricettario:

            if ingredient in self.ricettario[recipe_name]:

                self.ricettario[recipe_name].remove(ingredient)

                dizio: dict[str:list[str]] = {recipe_name: self.ricettario[recipe_name]}

                return f"{dizio}"

            else:

                return f'Errore: Questo ingrediente non è presente in questa ricetta'
                
        else:

            return f'Errore: Questa ricetta non esiste'
        
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str)->str:

        if recipe_name in self.ricettario:

            if old_ingredient in self.ricettario[recipe_name]:

                index: int = self.ricettario[recipe_name].index(old_ingredient)
                self.ricettario[recipe_name].remove(old_ingredient)
                self.ricettario[recipe_name].insert(index, new_ingredient)

                dizio: dict[str:list[str]] = {recipe_name: self.ricettario[recipe_name]}

                return f"{dizio}"

            else:

                return f'Errore: Questo ingrediente non è presente in questa ricetta'
                
        else:

            return f'Errore: Questa ricetta non esiste'
        

    def list_recipes(self):

        if self.ricettario:

            ricette: list[str] = []

            for key in self.ricettario:

                ricette.append(key)

            return ricette

        else:

            return f'Non sono presenti ricette'
        
    def list_ingredients(self, recipe_name: str): 

        if recipe_name in self.ricettario:

            return f'{self.ricettario[recipe_name]}'

        else:

            return f'Errore: Questa ricetta non esiste'
        
    def search_recipe_by_ingredient(self, ingredient: str):

        if self.ricettario:

            dizio: dict[str:list[str]] = {}
            
            for key in self.ricettario:

                if ingredient in self.ricettario[key]:

                    dizio[key] = self.ricettario[key]

            if dizio:

                return dizio
            
            else:

                return f'Non sono presenti ricette con questo ingrediente'

        else:

            return f'Non sono presenti ricette'


manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))