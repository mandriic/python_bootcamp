class Recipe:

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
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

test = Recipe("test", 1, 1, ["test", "test_mas", "mas_test"], "test_descrip", "test_type")
wtf = str(test)
print(wtf)