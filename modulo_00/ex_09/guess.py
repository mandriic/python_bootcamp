import random

print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number. \n
Type 'exit' to end the game.
Good luck!""")
num =  random.randint(1, 99)
print("What's your guess between 1 and 99?")
user_try = 0
trys = 0
while (user_try != num):
    user_try = input(">> ")
    if (user_try == "exit"):
        print("Goodbye!")
        exit()
    try:
        user_try = int(user_try)
    except:
        print("That's not a number.")
        continue
    trys += 1
    if user_try < num:
        print("Too low!")
    elif user_try == num:
        break
    else:
        print("Too high!")
if num == 42:
    print("The answer to the ultimate question of life, the universe and everything is 42.")
    if trys == 1:
        print("Congratulations! You got it on your first try!")
    else:
        print("You won in " + str(trys) + " attempts!")
else:
    print("Congratulations, you've got it!")
    if trys == 1:
        print("Congratulations! You got it on your first try!")
    else:
        print("You won in " + str(trys) + " attempts!")

