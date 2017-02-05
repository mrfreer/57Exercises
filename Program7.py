length = int(input("What is the length of the room in feet?"))
width = int(input("What is the width of the room in feet?"))
areaFT = length * width
areaMeters = areaFT * .09290304
print("You entered dimensions of " + format(length) + " feet by " + format(width) + " feet")
print("The area is \n" + format(areaFT) + " square feet")
print(format(areaMeters) + " square meters")