import sys

if len(sys.argv) > 3:
    print("AssertionError: too many arguments")
    exit()
elif len(sys.argv) != 3:
    print("""Usage: python operations.py <number1> <number2> Example:
\tpython operations.py 10 3""")
    exit()
elif sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False:
    print("AssertionError: only integers")
    exit()
    
try:
    print("Sum: \t\t" + str(int(sys.argv[1]) + int(sys.argv[2])))
except:
    print("Sum: ERROR (can't convert '" + sys.argv[1] + "' to an integer)")

try:
    print("Difference: \t" + str(int(sys.argv[1]) - int(sys.argv[2])))
except:
    print("Difference: ERROR (can't convert '" + sys.argv[1] + "' to an integer)")

try:
    print("Product: \t" + str(int(sys.argv[1]) * int(sys.argv[2])))
except:
    print("Product: ERROR (can't convert '" + sys.argv[1] + "' to an integer)")

try:
    print("Quotient: \t" + str(int(sys.argv[1]) / int(sys.argv[2])))
except:
    print("Quotient: ERROR (division by zero)")

try:
    print("Remainder: \t" + str(int(sys.argv[1]) % int(sys.argv[2])))
except:
    print("Remainder: ERROR (modulo by zero)")
    
    