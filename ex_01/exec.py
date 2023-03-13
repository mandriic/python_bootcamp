from curses.ascii import isupper
import sys
to_conv = sys.argv[1:]
ret = ""
for w in to_conv [::-1]:
    for let in w[::-1]:
        if let.isalpha():
            ret += let.swapcase()
        else: 
            ret += let
    ret += " "
print (ret[:-1])


