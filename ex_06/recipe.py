import json
from secrets import choice
def print_res(cookbook, key):
    print("\tRecipe for ", key)
    print("\tIngredients list: ", cookbook[key]["ingredients"])
    print("\tTo be eaten for", cookbook[key]["meal"])
    print("\tTakes ", cookbook[key]["prep_time"], " minutes of cooking.")

def print_all_res(cookbook):
    for key in cookbook.keys():
        print(key)

def add_res(cookbook):
    ingred = []
    print(">>> Enter a name: ")
    name = input()
    print(">>> Enter ingredients: ")
    while(True):
        ing = input()
        if ing == "":
            break
        else:
            ingred.append(ing)
    print(">>> Enter a meal type: ")
    type_m = input()
    print(">>> Enter a preparation time: ")
    try:
        time = int(input())
        if (time > 0):
            cookbook.update({name : {"ingredients": ingred, "meal" : type_m, "prep_time" : time}})
        else:
            print("Time only int positive") 
    except:
        print("Time only int positive")  
        
    
def del_res(cookbook, key):
    try:
        del cookbook[key]
    except:
        print("Receta no existe")

cookbook = {}

cookbook.update({"bocadillo": {
    "ingredients" : ['jamón', 'pan', 'queso', 'tomate'],
    "meal" : "almuerzo",
    "prep_time" : 10}
})

cookbook.update({"tarta": {
    "ingredients" : ['harina', 'azucar', 'huevos'],
    "meal" : "postre",
    "prep_time" : 60}
})

cookbook.update({"ensalada": {
    "ingredients" : ['aguacate', 'rúcula', 'tomates', 'espinacas'],
    "meal" : "almuerzo",
    "prep_time" : 15}
})

print ("Welcome to the Python Cookbook !\nList of available option:")
mess = """\t1: Add a recipe
\t2: Delete a recipe
\t3: Print a recipe
\t4: Print the cookbook
\t5: Quit"""
print (mess)
list_of_options = ['1','2','3','4','5']
while (True):
    print("Please select an option: ")
    choise = input(">> ")
    if choise not in list_of_options:
        print("Sorry, this option does not exist. \nList of available option: ")
        print (mess)
    elif choise == '2':
        print(">>> Enter a name to delete: ")
        del_res(cookbook, input())    
    elif choise == '1':
        add_res(cookbook)
    elif choise == '4':
        print_all_res(cookbook)
    elif choise == '3':
        print("Please enter a recipe name to get its details: ")
        choise = input(">> ")
        print_res(cookbook, choise)
    elif choise == '5':
        print("Cookbook closed. Goodbye !")
        exit()
        
    
