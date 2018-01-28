#!/opt/bin/python

def isPerm(first, second):
    firstL = sorted(first)
    secondL = sorted(second)

    if firstL == secondL:
        return True

    return False

word1 = "David"
word2 = "Gary"
word3 = "David"

print(isPerm(word1, word2))
print(isPerm(word1, word3))
