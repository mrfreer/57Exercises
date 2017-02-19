import string
from random import *
from random import shuffle


while True:
    try:
        minlength = int(input("What is the minimum length?"))
        spcharacters = int(input("How many special characters?"))
        numnumbers = int(input("How many numbers?"))
    except ValueError:
        print("All entries must be numeric:")
        continue
    else:
        break

specialcharacters = string.punctuation
numbers = string.digits
password = ""
password = "".join(choice(specialcharacters) for x in range(spcharacters))
password = "".join(choice(numbers) for x in range(numnumbers)) + password
password = "".join(choice(string.ascii_letters) for x in range(minlength-(spcharacters+numnumbers))) + password
l = list(password)
shuffle(l)
newpass = "".join(l)
print(newpass)