from datetime import datetime, timedelta

#figure out today and figure out when the first and last day of this week (Assuming week start Saturday and ends Sunday)

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


#make a list of each day this week

datesInWeek =[]

for x in range (0, 7):
    datesInWeek.append((beginWeek + timedelta(days = x)).strftime('%Y-%m-%d'))

print(datesInWeek)
