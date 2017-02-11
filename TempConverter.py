#Temperature Converter
while True:
    try:
        temp = int(input("Enter the temperature:"))
    except ValueError:
        continue
    else:
        break
convert = input("To F or C")
if convert == 'F':
    print(str(temp*(9/5) +32))
elif convert == 'C':
    print(str((temp-32)*5/9))
else:
    print("Invalid entry")