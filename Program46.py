from collections import Counter
F = open("words.txt", "r+")
readin = F.read()
words = readin.split()
sortedfun = sorted(words, key=words.count, reverse = True)
#We want the most common word on top.
uniqwords = set(sortedfun)

for i in uniqwords:

    stars = ""
    for j in range(words.count(i)):
        stars += "*"
    print(i + ":" + stars)
