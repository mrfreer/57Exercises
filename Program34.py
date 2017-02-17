employees = ['John Smith', 'Jackie Johnson', 'Chris Jones', 'Amanda Cullen', 'Jeremy Goodwin']
print("There are " + str(len(employees)) + " employees.")
for i in employees:
    print(i)
nameemp = input("Enter an employee name to remove:")

if nameemp in employees:
    employees.remove(nameemp)
else:
    print("Employee not in list.")
print("There are " + str(len(employees)) + " employees.")
for i in employees:
    print(i)