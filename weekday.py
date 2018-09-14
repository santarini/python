from datetime import datetime, timedelta
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"]
today = datetime.today().weekday()
todayDate = datetime.today()
beginWeek = datetime.today() - timedelta(days=(today+1))
endWeek = beginWeek + timedelta(days=6)
print("Today is " + weekdays[today])
print(today)
print("Today's date is " + todayDate.strftime("%Y-%m-%d"))
print("Sunday's date is " + beginWeek.strftime("%Y-%m-%d"))
print("Saturday's date is " + endWeek.strftime("%Y-%m-%d"))
