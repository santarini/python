###user selects FV calculator

    print("\n" + "FUTURE VALUE CALCULATOR" + "\n")
    pv = int(input("How much money are you starting with?" "\n"))
    pr = int(input("What percentage interest rate can you achieve per year?"+ "\n"))
    i = (pr/100)
    n = int(input("How many years do you plan to maintain the position?" + "\n"))
    pmtQ = input("Are you planning on making regular contributions or withdrawls from the intial investment? y/n" + "\n")
    if pmtQ == "y" or pmtQ == "Y" or pmtQ == "yes" or pmtQ == "Yes":
        #k = int(input("How many times per year are you planning to withdraw or deposit?" + "\n"))
        pmt = int(input("How much are you planning to withdraw or deposit (net contribution)?" + "\n"))
        fv0 = (pv * ((1 + i)**n))
        fvPMT = (pmt *((((1 + i)**n)-1)/i))
        fv = (fv0 + fvPMT)
         print("In " + str(n) + " years, with a " + pmt + " every year, your " + str(pv) + " investment will be worth " + str(fv))
    else:
        fv = (pv * ((1 + (i))**n))
        print("In " + str(n) + " years, your " + str(pv) + " investment will be worth " + str(fv))
