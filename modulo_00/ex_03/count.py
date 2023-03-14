from multiprocessing.context import SpawnContext
from string import punctuation
import sys

def text_analyzer(*args, **kwargs):
    all_c = 0
    upper = 0
    lower = 0
    punct = 0
    spaces = 0
    for let in args[0]:
        all_c += 1
        if let.isupper():
            upper += 1
        elif let.islower():
            lower += 1
        elif let.isspace():
            spaces += 1
        elif let in punctuation:
            punct += 1
    print ("The text contains " + str(all_c) + " character(s):")
    print("- " + str(upper) + " upper letter(s)")
    print("- " + str(lower) + " lower letter(s)")
    print("- " + str(punct) + " punctuation mark(s)")
    print("- " + str(spaces) + " space(s)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("ERROR")
        exit()
    text_analyzer(sys.argv[1])