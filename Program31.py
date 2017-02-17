import math


while True:
    try:
        restingpulse = int(input("Enter resting pulse:"))
        age = int(input("Enter age:"))
    except ValueError:
        print("Only enter numbers.")
        continue
    else:
        break

print("Resting pulse: " + str(restingpulse) + " Age: " + str(age))
print("Intensity\t | Rate")
print("------------------------")
for i in range(55,95,5):
    targetrate = (((220-age)-restingpulse)*i/100)+restingpulse
    print(str(i) + "%\t\t\t | " + str(int(round(targetrate, 0))) + " bpm")
