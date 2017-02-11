while True:
    try:
        principal = int(input("Enter the principal:"))
        rate = float(input("Enter the rate of interest:"))
        years = int(input("Enter the number of years:"))
    except ValueError:
        print("All entries must be numbers.")
        continue
    else:
        break

interest = principal * (1 + rate * years)
print("After " + str(years) + " years at " + str(100*rate) + "%, the investment will be worth $" + "{0:.2f}".format(interest) + ".")
