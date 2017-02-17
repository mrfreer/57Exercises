a = []

line = "       "
for i in range(0,13):
    if i < 10:
        line += (str(i) + "   ")
    else:
        line += (str(i) + "  ")

print(line)
a = []
for i in range(0,13):
    a.append(i)
    for j in range(0, 13):
        a.append(i * j)
    line = ""

    for j in a:
        if j < 10:
            line = line + "   " + str(j)
        elif j < 100:
            line = line + "  " + str(j)
        else:
            line = line + " " + str(j)
    print(line)
    a = []

