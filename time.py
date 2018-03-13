import datetime

timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
current_month = datetime.datetime.now().month
current_year = datetime.datetime.now().year
current_day = datetime.datetime.now().day

print(timenow)
print(current_month)
print(current_year)
print(current_day)
