rateofreturn = 0
while True:
    try:
        rateofreturn = int(input("What is the rate of return?"))
        if rateofreturn <= 0:
            print("Sorry. That's not a valid input.")
            continue
    except ValueError:
        print("Sorry. That's not a valid input.")
        continue
    else:
        years = 72 / rateofreturn
        print("It will take " + str(years) + " years to double your initial investment.")
        break

