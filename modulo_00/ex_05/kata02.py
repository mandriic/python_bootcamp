# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

from datetime import datetime

date = datetime(kata[0], kata[1], kata[2], kata[3], kata[4])
print(date.strftime("%m/%d/%Y %H:%M"))
