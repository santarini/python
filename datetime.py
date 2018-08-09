#https://docs.python.org/2/library/datetime.html

import datetime

dayofWeek = datetime.datetime.today().weekday()
fullDate = datetime.datetime.now().strftime("%Y-%m-%d")

print(str(dayofWeek) + " " + fullDate)
