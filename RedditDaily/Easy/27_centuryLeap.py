import math
import datetime

def centuryCal():
    yearInput = input("Enter year: \n")

    century = int(yearInput)/100

    now = datetime.datetime.now()

#check century
    if int(yearInput) > int(now.year):
        print(str(yearInput)+ " will be in the " + str(math.ceil(century)) + "th Century")
    elif int(yearInput) > int(now.year):
        print(str(yearInput)+ " is in the " + str(math.ceil(century)) + "th Century")
    elif math.ceil(century) > 3:
        print(str(yearInput)+ " was in the " + str(math.ceil(century)) + "th Century")
    elif math.ceil(century) == 3:
        print(str(yearInput)+ " was in the " + str(math.ceil(century)) + "rd Century")
    elif math.ceil(century) == 2:
        print(str(yearInput)+ " was in the " + str(math.ceil(century)) + "nd Century")
    elif math.ceil(century) == 1:
        print(str(yearInput)+ " was in the " + str(math.ceil(century)) + "st Century")

#check if leap year
    if not(int(yearInput) % 4 == 0):
        print(str(yearInput)+ " is a Common Year")
    elif not(int(yearInput) % 100 == 0):
        print(str(yearInput)+ " is a Leap Year")
    elif not(int(yearInput) % 400 == 0):
        print(str(yearInput)+ " is a Common Year")
    else:
        print(str(yearInput)+ " is a Common Year")

    print("\n")
    
    centuryCal()
centuryCal()
