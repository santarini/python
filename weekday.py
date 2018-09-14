import datetime
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"]
today = datetime.datetime.today().weekday()
print(weekdays[today])
