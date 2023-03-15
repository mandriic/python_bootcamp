class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list
    
    def get_recipe_by_name(self, name):
        """Imprime la receta con el nombre \texttt{name} y devolver la instancia"""
        #... Aqui tu código ...
    def get_recipes_by_types(self, recipe_type):
        """Devuelve todas las recetas dado un recipe_type """
        #... Aqui tu código ...
    def add_recipe(self, recipe):
        """Añade una receta al libro y actualiza last_update"""
        #... Aqui tu código ...