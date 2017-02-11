
total = 0
for i in range(1,4):
    while True:
        try:
            price = int(input("Enter the price of item " + str(i) + ":"))
            quantity = int(input("Enter the quantity of item " + str(i) + ":"))
        except ValueError:
            print("Price and quantity must be numeric:")
            continue
        else:
            total += (price * quantity)
        break
print("Subtotal: $" + "{0:.2f}".format(total))
tax = total * .055
print("Tax: $" + "{0:.2f}".format(tax))
total += tax
print("Total: $" + "{0:.2f}".format(total))