import math
import datetime

def centuryCal():
    yearInput = input("Enter year: \n")
    century = math.ceil(int(yearInput)/100)
    now = datetime.datetime.now()

#tense modifier
    if int(yearInput) == int(now.year):
        tense = " is "
    if int(yearInput) < int(now.year):
        tense = " was "
    if int(yearInput) > int(now.year):
        tense = " will be "

#determine century
    if str(century).endswith("3") and not(str(century).startswith("1")):
        print(yearInput + tense + "in the " + str(century) + "rd Century")
    if str(century).endswith("2") and not(str(century).startswith("1")):
        print(yearInput + tense + "in the " + str(century) + "nd Century")
    if str(century).endswith("1") and not(str(century).startswith("1")) or century == 1 :
        print(yearInput + tense + "in the " + str(century) + "st Century")
    if century > 3:
        print(yearInput + tense + "in the " + str(century) + "th Century")

#check if leap year
    if not(int(yearInput) % 4 == 0):
        print(str(yearInput) + tense +  "a Common Year")
    elif not(int(yearInput) % 100 == 0):
        print(str(yearInput) + tense +  "a Leap Year")
    elif not(int(yearInput) % 400 == 0):
        print(str(yearInput) + tense +  "a Common Year")
    else:
        print(str(yearInput) + tense + "a Common Year")

#give some breathing room
    print("\n")

    centuryCal()
centuryCal()
