n = 1
for i in range (65,90):
    for j in range (65,90):
        for k in range (65,90):
            test = str(n) + ': ' + chr(i) + chr(j) + chr(k)
            print (test)
            n +=1
