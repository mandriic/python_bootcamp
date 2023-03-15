class Recipe:

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = ""):
        if not isinstance(cooking_time, int) or cooking_time < 0:
            print("El tiempo de cocción debe ser un número entero positivo")
            exit()
        if not isinstance(name, str):
            print("Nombre debe ser un string")
            exit()
        if not isinstance(cooking_lvl, int) or cooking_lvl < 1 or cooking_lvl > 5:
            print("El nivel de cocción debe ser un número entero entre 1 y 5")
            exit()
        if not isinstance(ingredients, list):
            print("Ingredientes debe ser una lista")
            exit()
        if not isinstance(recipe_type, str) or recipe_type not in ["entrante", "comida", "postre"]:
            print("El tipo de receta debe ser un string y debe ser entrante, comida o postre")
            exit()
        if not isinstance(description, str):
            print("La descripción debe ser un string")
            exit()
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        print(self.name)
        txt = "txt to return"
        """Your code here"""
        return txt

test = Recipe("test", 1, 0, ["test", "test_mas", "mas_test"], "entrante", "333")
test2 = Recipe("test", 1, 0, ["test", "test_mas", "mas_test"], "entrante", "333")
test.description = "test_description"
print(test2.description)
print(test.description)
wtf = str(test)
print(wtf)




# class Recipe:
#     def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
#         self.name = name
#         self.cooking_lvl = cooking_lvl
#         self.cooking_time = cooking_time
#         self.ingredients = ingredients
#         self.description = description
#         self.recipe_type = recipe_type

#     def __str__(self):
#         return f'{self.name} ({self.recipe_type}): {self.description}\nCooking Level: {self.cooking_lvl}, Cooking Time: {self.cooking_time} minutes\nIngredients: {", ".join(self.ingredients)}'

#     def display_recipe(self):
#         print(self.__str__())