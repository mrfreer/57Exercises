import json
from pprint import pprint

with open('products.json') as data_file:
    data = json.load(data_file)



while True:
    userprod = input("What is the product name?  Enter quit to exit.")
    if userprod == "quit":
        break
    isfound = False
    for i in data["products"]:
        if i['name'] == userprod:
            print("That product is in our inventory. $" + str(i['price']))
            isfound = True
    if isfound == False:
        print("Sorry, that product is not in our inventory.")
