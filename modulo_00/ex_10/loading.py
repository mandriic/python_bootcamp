import time as t
import sys
def ft_progress(listy):
    print("Loading")
    kata = ">"
    cerr = "]"    
    time_s = t.time()
    i = 1
    f_pr = 0
    proc = 1
    for elem in listy:
        time_n = t.time()
        time_c = time_n - time_s
        if listy[-1]/42 * i <= elem:
            i += 1
        if int((elem/listy[-1]) * 100) == proc:
            f_pr = time_c / ((elem/listy[-1]) * 100)
            proc += 1
        est_t = f_pr * (100 - (int((elem/listy[-1]) * 100)))
            # f_pr =  time_c / ((elem/listy[-1]) * 100)
        string = "[" + kata.rjust(i, '=') + cerr.rjust(42 - i + 2, " ")
        est_time = f_pr * time_c
        sys.stdout.write("ETA: {:.2f}s  [{:.0f}%] {} [{}/{}]| elapsed time {:.2f}s \r".format(est_t, elem/listy[-1] * 100, string, elem + 1, listy[-1] + 1, time_c))
        
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