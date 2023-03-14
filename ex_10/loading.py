import time as t
import sys
def ft_progress(listy):
    print(listy)
    print("Loading")
    kata = ">"
    cerr = "]"    
    time_s = t.time()
    i = 1
    for elem in listy:
        time_n = t.time()
        time_c = time_n - time_s
        if listy[-1]/42 * i <= elem:
            i += 1
        string = "[" + kata.rjust(i, '=') + cerr.rjust(42 - i + 2, " ")
        sys.stdout.write("ETA: {:.2f}s [{:.0f}%] {s}\r".format(time_c, elem/listy[-1] * 100, s=string))
        
        sys.stdout.flush()
        # sys.stdout.write("ETA: %d%% %d  \r" % (elem) % (time_s)  )
        # sys.stdout.flush()
        yield elem
    
listy = range(1000)
ret = 0
for elem in ft_progress(listy): 
    ret+=(elem+3) %5
    t.sleep(0.01)
print()
print(ret)

# # Put this at the top of your kata03.py file
# import time as t
# kata = ">"
# cerr = "]"
# for i in range(42):
#     print("[", kata.rjust(i, '='), cerr.rjust(42 - i, " "), flush=True)
#     t.sleep(1)