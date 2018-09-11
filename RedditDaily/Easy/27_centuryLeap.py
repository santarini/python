import math

def centuryCal():
    yearInput = input("Enter year: \n")

    century = int(yearInput)/100

#check century
    if math.ceil(century) > 3:
        print(str(yearInput)+ " was in the year " + str(math.ceil(century)) + "th Century")
    elif math.ceil(century) == 3:
        print(str(yearInput)+ " was in the year " + str(math.ceil(century)) + "rd Century")
    elif math.ceil(century) == 2:
        print(str(yearInput)+ " was in the year " + str(math.ceil(century)) + "nd Century")
    elif math.ceil(century) == 1:
        print(str(yearInput)+ " was in the year " + str(math.ceil(century)) + "st Century")

#check if leap year
    if not(int(yearInput) % 4 == 0):
        print("Common Year")
    elif not(int(yearInput) % 100 == 0):
        print("Leap Year")
    elif not(int(yearInput) % 400 == 0):
        print("Common Year")
    else:
        print("Common Year")

    print("\n")
    
    centuryCal()
centuryCal()

