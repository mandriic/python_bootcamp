import sys
if (sys.argv[1].isdigit() == False):
    print("AssertionError: argument is not an integer")
elif (len(sys.argv) > 2):
    print("AssertionError: more than one argument are provided")
elif (int(sys.argv[1]) == 0):
    print("I'm Zero.")
elif (int(sys.argv[1]) % 2 == 0):
    print("I'm Odd.")
elif (int(sys.argv[1]) % 2 != 0):
    print(("I'm Even."))
elif (int(sys.argv[1]) < 0):
    print("I'm Negative.")