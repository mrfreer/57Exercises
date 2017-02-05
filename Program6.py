import datetime

curAge = int(input("What is your current age?"))
retireAge = int(input("At what age would you like to retire?"))
now = datetime.datetime.now()
curYear = now.year

yearsToRetire = retireAge - curAge
retirementYear = now.year + yearsToRetire
print("You have " + format(yearsToRetire) + " years left until you retire.")
print("It's " + format(now.year) + ", so you can retire in " + format(retirementYear))
