import random
 
length = int(input("How many characters lond do you want your password(s) to be? \n"))
qty = int(input("How many passwords do you want to generate? \n"))
spec = input("Can your password contain special characters? \n")
num = input("Does your password need to include numbers? \n")

txt = open('pass.txt', 'a')

i = 0
while i < qty:
    j = 0
    password = ''
    while j < length:
        if num == "No" and spec == "No":
            password += chr(random.choice([random.randint(65,90),random.randint(141,171)]))
        if spec == "Yes" and num == "No":
            password += chr(random.choice([random.randint(33,47),random.randint(91,96),random.randint(123,126),random.randint(65,90),random.randint(141,171)]))
        if spec == "No" and num == "Yes":
            password += chr(random.choice([random.randint(48,57),random.randint(65,90),random.randint(141,171)]))
        if spec == "Yes" and num == "Yes":
            password += chr(random.randint(33, 125))
        j += 1
    txt.write(password + '\n')
    i += 1
txt.close()
