#anagram checker
from collections import Counter


def ispalindrome(word1, word2):
    tocheck = ''.join(reversed(word2))
    if word1 == tocheck:
        return True
    else:
        return False

def isanagram(word1, word2):
    return Counter(word1) == Counter(word2)

word = input("Enter a word:")
wordA = input("Enter a second word:")

if ispalindrome(word, wordA):
    print("The two are palindromes.")
else:
    print("The two are not palindromes.")

if isanagram(word, wordA):
    print("The two are anagrams.")
else:
    print("The two are not anagrams.")