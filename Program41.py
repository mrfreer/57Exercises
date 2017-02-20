#read the names.txt and sort them.
#display the names and number of names.
names = []
file = open("names.txt", "r")
for line in file:
    names.append(line.rstrip()) #take out the newline
names.sort()
print("There are " + str(len(names)) + " names in the file.")
for name in names:
    print(name)
