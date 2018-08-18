import schedule
import datetime

#NYSE,NASDAQ,AMEX (Hours 9:30am-4:00pm)

weekdays = ['monday','tuesday','wednesday','thursday','friday']

##print("17:00")

def job():
    n = datetime.datetime.now()
    print("Test " + str(n))

for k in range(0,5):
    dayHolder = weekdays[k]
    print(dayHolder)
    schedule.dayHolder.at(timeHolder).do(job)
