#Blood Alcohol Calculator
while True:
    try:
        A = int(input("How much alcohol (in ounces)?"))
        W = int(input("What is your body weight in pounds?"))
        r = float(input("What is the alcohol distribution ratio? .73 for men .66 for women."))
        H = float(input("How many hours since the last drink?"))
    except ValueError:
        print("Each value must be numeric")
        continue
    else:
        break
BAC = (A * 5.14/W * r)-.15*H
if BAC > .08:
    print("It is not legal for you to drive.")
else:
    print("It is legal for you to drive.")