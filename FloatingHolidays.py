import datetime
marketHolidays = []
dayOccurences = []

#Get year
now = datetime.datetime.now()

#check if leap year
if not(int(now.year) % 4 == 0):
    print(str(now.year) + " Common Year")
    febDays = 28
elif not(int(now.year) % 100 == 0):
    print(str(now.year) + " Leap Year")
    febDays = 29
elif not(int(now.year) % 400 == 0):
    print(str(now.year) + " Common Year")
    febDays = 28
else:
    print(str(now.year) + " Common Year")
    febDays = 28

##### Determine holidays

daysInWeek = ["Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
        ]

monthsInYear = {'January': [31, 1],
                'February': [febDays, 2],
                'March': [31, 3],
                'April': [30, 4],
                'May': [31, 5],
                'June': [30, 6],
                'July': [31, 7],
                'August': [31, 8],
                'September': [30, 9],
                'October': [31, 10],
                'November': [30, 11],
                'December': [31, 12]
                }

#holidays data

holidaysData = [["New Year's Day", "Fixed", datetime.date(now.year, 1, 1), "Closed"],
                ["Martin Luther King, Jr. Day", "Variable", 'January', 'Monday', 3, "Closed"],
                ["President's Day", "Variable", 'February', 'Monday', 3, "Closed"],
                #["Good Friday", "Variable", '', '', 0, "Closed"],
                ["Memorial Day", "Variable", 'May', 'Monday', -1, "Closed"],
                ["Independence  Day", "Fixed", datetime.date(now.year, 7, 4), "Closed"],
                ["Labor  Day", "Variable", 'September', 'Monday', -2, "Closed"],
                ["Thanksgiving", "Variable", 'November', 'Thursday', 4, "Closed"],
                ["Christmas", "Fixed", datetime.date(now.year, 12, 25), "Closed"]
                ]

# run dynamic holidays function

for x in range(0,8):
    if holidaysData[x][1] == "Fixed":
        #If the holiday falls on a Saturday, the market will close on the preceding Friday.
        if holidaysData[x][2].weekday() == 5:
            marketHolidays.append((holidaysData[x][2]) + datetime.timedelta(days=-1))
        #If the holiday falls on a Sunday, the market will close on the subsequent Monday.
        if holidaysData[x][2].weekday() == 6:
            marketHolidays.append((holidaysData[x][2]) + datetime.timedelta(days=1))
        else:
            marketHolidays.append(holidaysData[x][2])
    else:
        floatingHoliday(holidaysData[x][2],holidaysData[x][3],holidaysData[x][4])
