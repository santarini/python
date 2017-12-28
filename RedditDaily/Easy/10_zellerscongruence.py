#uses Zeller's congruence
day = int(input("Day \n"))
month = int(input("Month \n"))
year = int(input("Year \n"))
y1 = int(str(year)[:2])
y2 = int(str(year)[2:])
monthList = [11,12,1,2,3,4,5,6,7,8,9,10]
m = monthList[month-1]
f = (day + ((13 * (m -1))/5) + int(y2) +(int(y2)/4)+(int(y1)/4)-(2 * int(y1)))%7
dayList = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
w = dayList[int(f)]
print(w)
