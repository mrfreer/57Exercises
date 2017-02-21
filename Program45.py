infile = input("Name of file to read in:")

F = open(infile, "r+")
readin = F.read()
F.close()
open(infile, 'w')
F = open(infile, "r+")
F.write(readin.replace("utilize", "use"))
F.close()