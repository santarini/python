import math

def centuryCal():
    yearInput = input("Enter year: \n")

    century = int(yearInput)/100

    if math.ceil(century) > 3:
        print(str(yearInput)+ " was in the year " + str(math.ceil(century)) + "th Century")
    elif math.ceil(century) == 3:
        print(str(yearInput)+ " was in the year " + str(math.ceil(century)) + "rd Century")
    elif math.ceil(century) == 2:
        print(str(yearInput)+ " was in the year " + str(math.ceil(century)) + "nd Century")
    elif math.ceil(century) == 1:
        print(str(yearInput)+ " was in the year " + str(math.ceil(century)) + "st Century")
    print("\n")
    centuryCal()
centuryCal()
