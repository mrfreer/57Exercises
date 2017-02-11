import getpass


pw = getpass.getpass('What is the password?')
if pw == "abc$123":
    print("Welcome!")
else:
    print("I don't know you.")