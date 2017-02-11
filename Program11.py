#euros to dollars

while True:
    try:
       numeuros = int(input("Enter the number of euros?"))
       exchangerate = float(input("What is the exchange rate?"))
    except ValueError:
        print("Both number of euros and the exchange rate must be numeric:")
        continue
    else:
        break
amountto = numeuros * exchangerate
print(str(numeuros) + " euros is " + str(amountto) + " dollars")