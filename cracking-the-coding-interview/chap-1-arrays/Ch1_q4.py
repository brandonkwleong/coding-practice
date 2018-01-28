#!/opt/bin/python

def isPalin(word):

    word_nospaces = word.replace(' ', '')
    wordnsL = list(word_nospaces)

    counter = dict()
    for c in wordnsL:
        if c not in counter.keys():
            counter[c] = 1
        else:
            counter[c] += 1
    
    # even length string
    if len(wordnsL) % 2 == 0:
        for key, value in counter.items():
            if value % 2 != 0:
                return False
        return True

    # odd length string
    else:
        oddFound = False
        for key, value in counter.items():
            if value % 2 != 0:
                if oddFound == False:
                    oddFound = True
                else:
                    return False

        return True

# =================

print(isPalin("taco cat"))
print(isPalin("tttattt"))
print(isPalin("brandon"))
    
