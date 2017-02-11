import math
while True:
    try:
        principal = float(input("What is the principal?"))
        rate = float(input("What is the rate?"))
        years = int(input("How many years?"))
        numtimes = float(input("What is the number of times the interest is compounded per year?"))
    except ValueError:
        print("All need to be entered as numbers.")
        continue
        #A = P(1+r/n)^nt
    else:
        break
amount = principal * pow((1 + rate / numtimes), (numtimes*years))
print("$" + str(principal) + " invested at " + str(rate* 100) + "% is $" + "{0:.2f}".format(mathamount))
