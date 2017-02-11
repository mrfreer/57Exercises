import math
while True:
    try:
        length = int(input("Enter length of room (in feet):"))
        width = int(input("Enter the width of room (int feet):"))
    except ValueError:
        print("All entries must be numeric")
        continue
    else:
        break
sqfeet = length * width
gallons = math.ceil(sqfeet / 350)
print("You will need to purchase " + str(gallons) + " gallons of paint to cover " + str(sqfeet) + " sq. ft.")
