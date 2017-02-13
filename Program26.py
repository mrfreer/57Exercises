import math


while True:
    try:
        b = float(input("What is your balance?"))
        i = float(input("What is the APR on the card (as a percent)?"))
        p = float(input("What is the monthly payment you can make?"))
    except ValueError:
        print("All entries must be numeric.")
        continue
    else:
        break
i = i / 100.0
i = i / 365.0
n = (-1/30) * ((math.log(1.0+float(b/p) * (1-math.pow((1+i), 30.0))))/(math.log(1+i)))
n = math.ceil(n)
print("It will take you " + str(n) + " months to pay off this card.")
