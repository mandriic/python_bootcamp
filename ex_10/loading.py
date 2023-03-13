import time
def progress_bar(lst):
    print("Loading")
    for elem in lst:
        yield elem
        # print(".", end="", flush=True)
    
    
    
    
listy = range(1000)
ret = 0
for elem in progress_bar(listy): 
    print(elem, end=" ", flush=True)
    ret += elem 
    time.sleep(0.01)
print()
print(ret)