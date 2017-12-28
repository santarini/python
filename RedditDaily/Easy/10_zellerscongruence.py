month = int(input("Month \n"))
day = int(input("Day \n"))
year = int(input("Year \n"))
if month == 1 or month == 2:
    year = year -1
y1 = year%100 #int(str(year)[:2])
y2 = year/100 #int(str(year)[2:])
print(y1, y2)
monthList = [13,14,3,4,5,6,7,8,9,10,11,12]
m = monthList[month-1]
f = (day + int(13*(m+1)/5) + int(y1) +(int(y1)/4)+(int(y2)/4)-(2 * int(y2)))%7
dayList = ["Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(f)
w = dayList[int(f) -1]
print(w)
