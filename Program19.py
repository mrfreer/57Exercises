#BMI Calculator
while True:
    try:
        weight = int(input("Enter your weight (pounds):"))
        height = int(input("Enter your height (inches):"))
    except ValueError:
        print("Only numeric values accepted.")
        continue
    else:
        break
bmi = (weight/(height* height))*703
if bmi >= 18.5 and bmi <=25:
    print("You're a normal weight.")
elif bmi < 18.5:
    print("You are underweight.")
else:
    print("You are overweight.")