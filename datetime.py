import random
import datetime

dayofWeek = datetime.datetime.today().weekday()
fullDate = datetime.datetime.now().strftime("%Y-%m-%d")
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"]
print(weekdays[dayofWeek] + " " + fullDate)
