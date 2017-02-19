print("Enter a list of numbers, separated by spaces:")
listnums = [int(x) for x in input().split()]
allevens = [int(x) for x in listnums if int(x) % 2 == 0]
print(allevens)