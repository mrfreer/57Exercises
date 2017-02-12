#Comparing numbers
while True:
    try:
        num1 = int(input("Enter the first number"))
        num2 = int(input("Enter the second number"))
        num3 = int(input("Enter the third number"))
    except ValueError:
        print("All entries must be numeric.")
        continue
    else:
        break

allnums = []
allnums.append(num1)
allnums.append(num2)
allnums.append(num3)
makeset = set(allnums)
if len(makeset) != 3:
    print("All numbers must be different.")
else:
    largest = allnums[0]
    for i in allnums:
        if i > largest:
            largest = i
    print(str(largest) + " is the largest number entered.")