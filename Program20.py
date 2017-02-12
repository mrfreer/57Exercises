#Enter your income and get back your tax bracket for the 2016 year
import json
import urllib
import requests
headers={"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBUElfS0VZX01BTkFHRVIiLCJodHRwOi8vdGF4ZWUuaW8vdXNlcl9pZCI6IjU4YTA0YWRhMmIyYzIyMWVkOWI0OTg2OSIsImh0dHA6Ly90YXhlZS5pby9zY29wZXMiOlsiYXBpIl0sImlhdCI6MTQ4Njg5OTkzMH0.oKBamJftX_mpURhAv4HJ4yfS6R5VBDtWwTKeWLN4iCQ"}
r = requests.get(url='http://taxee.io/api/v2/federal/2016',headers=headers)
data = r.json()
while True:
    try:
        income = int(input("Enter your income:"))
    except ValueError:
        print("Entries must be numeric")
        continue
    else:
        break

brackets = [i['bracket'] for i in data['single']['income_tax_brackets']]
print(brackets)
#userbracket = [i for i in data['single']['income_tax_brackets']['bracket'] if income > i]
for i in data['single']['income_tax_brackets']:
    if income < i['bracket']:
        print(str(i['marginal_rate']) + " is your marginal rate.")
        print(str(i['bracket']) + "% is your tax bracket for your " + str(income))
        break
