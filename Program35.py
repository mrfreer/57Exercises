import random

names = []
while True:
    usename = input("Enter a name:")
    if len(usename) > 0:
        names.append(usename)
    else:
        break

print("The winner is..." + names[random.randint(0, len(names) -1 )])