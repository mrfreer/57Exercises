import re
#Validating Input
def checkfirst(first):
    if len(first) >= 2:
        return True
    else:
        return False

def checklast(last):
    if len(last) >= 2:
        return True
    else:
        return False


def checkempid(id):
    prog = re.compile("[a-zA-Z]{2}\-[0-9]{4}")
    if prog.search(id):
        return True
    else:
        return False

def checkzipcode(zip):
    if zip.isnumeric() and len(zip) == 5:
        return True
    else:
        return False


f = input("Enter the first name:")
l = input("Enter the last name:")
z = input("Enter the ZIP code:")
id = input("Enter an employee ID:")
if checkfirst(f) != True:
    print(f + " is not a valid name.  It is too short.")
elif checklast(l) != True:
    print(l + " is not a valid name.  It is too short.")
elif checkzipcode(z) != True:
    print(z + " is not a valid ZIP code.")
elif checkempid(id) != True:
    print(id + " is not a valid ID.")
else:
    print("There were no errors found.")

