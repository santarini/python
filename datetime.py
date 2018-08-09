#https://docs.python.org/2/library/datetime.html
import datetime

dayofWeek = datetime.datetime.today().weekday()
fullDate = datetime.datetime.now().strftime("%Y-%m-%d")
timeNow = datetime.datetime.now().strftime("%H:%M:%S")
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"]
print(weekdays[dayofWeek] + " " + fullDate + " " + timeNow)
