
while True:
    try:
        numpeople = int(input("How many people?"))
        numpizzas = int(input("How many pizzas?"))
        numslices = int(input("How many slices?"))
    except ValueError:
        print("All entries must be numeric:")
        continue
    else:
        break


totslices = numpizzas * numslices
perperson = int((totslices / numpeople))
remainder = totslices - (perperson * numpeople)
print("Each person gets " + str(perperson) + " slices.")
print("There are " + str(remainder) + " leftover pieces.")