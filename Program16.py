#Legal driving age
while True:
    try:
        age = int(input("What is your age?"))
    except ValueError:
        print("Enter a number")
        continue
    else:
        break

if age < 0:
    print("Incorrect entry.")
elif age < 16:
    print("You are not old enough to legally drive")
else:
    print("You are old enough to legally drive.")