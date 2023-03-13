import sys
import time
progres = 0
for i in range(100):
    progress = i + 1
    sys.stdout.write("Download progress: %d%%   \r" % (progress) )
    sys.stdout.flush()
    time.sleep(0.1)    