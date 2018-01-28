#!/opt/bin/python

def replaceSpaces(word, length):
    
    resultString = []
    wordL = list(word)
    
    index = 0
    while index < length:
        if wordL[index] != ' ':
            resultString.append(wordL[index])
            index += 1
        else:
            resultString.extend(['%', '2', '0'])
            while word[index] == ' ':
                index += 1

    return ''.join(resultString)

# ==========

word1 = "Brandon Alice"
word2 = "Jump    For Joy  "

print("[{0}]".format(replaceSpaces(word1, 13)))
print("[{0}]".format(replaceSpaces(word2, 15)))
