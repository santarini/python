import re
import datetime

dateList = []

today = datetime.date.today()

#were given a list of values
workingList = ['08/12/2018 - 08/18/2018 (Open)', '08/19/2018 - 08/25/2018 (Open)', 'Archived time cards']


#we figure out which list contians dates and plug those into a list
r = re.compile("\d\d/\d\d/\d\d\d\d - \d\d/\d\d/\d\d\d\d")
newlist = list(filter(r.match, workingList))

#we figure out the index ref number for each list element and create a dictionary 
for element in newlist:
    subList = [workingList.index(element)]
    dateStr = element.split("(")[0].split("-")[0].rstrip()
    dateStart = datetime.datetime.strptime(dateStr, '%m/%d/%Y').date()
    for x in range (0, 7):
        subList.append((dateStart + datetime.timedelta(days = x)).strftime('%Y-%m-%d'))
    dateList.append(subList)

for sublist in dateList:
    if str(today) in sublist:
        print(sublist[0])



