#works from 1582-3999
month = int(input("Month \n"))
day = int(input("Day \n"))
year = int(input("Year \n"))
if month == 1 or month == 2:
    year = year -1
if year >= 2000:
    K =  int(str(year)[:2])
    J =  int(str(year)[2:])
if year < 2000:
    K =  year%100
    J =  year/100
monthList = [13,14,3,4,5,6,7,8,9,10,11,12]
m = monthList[month-1]
dayList = ["Saturday", "Sunday", "Monday", "Tuesday","Wednesday", "Thursday", "Friday"]

A = ((13 * m) -1)//5
B = K
C = K//4
D = J//4
E = 2 * J
Z = A + B + C + D - E
w = dayList[(int(Z) % 7)-1]
print(w)
