#tax calculator
while True:
    try:
        order = float(input("What is the order amount?"))
    except ValueError:
        print("Order must be a number.")
        continue
    else:
        break
    