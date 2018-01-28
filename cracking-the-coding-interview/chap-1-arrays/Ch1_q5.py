#/opt/bin/python

def oneAway(word1, word2):

    word1len = len(word1)
    word2len = len(word2)
    
    if abs(word1len - word2len) > 1:
        return False

    maxLength = word1len if word1len > word2len else word2len

    word1L = list(word1)
    word2L = list(word2)
    diffFound = 0
    for i in range(maxLength):
        
        if diffFound > 1:
            return False

        if i == word1len or i == word2len:
            break
        
        print(word1L)
        print(word2L)
        print("========")
        if word1L[i] == word2L[i]:
            continue

        if word1len > word2len:
            del word1L[i]
            diffFound += 1
            i -= 1
        elif word1len < word2len:
            del word2L[i]
            diffFound += 1
            i -= 1
        else:
            diffFound += 1

    return True

 # ====================

print(oneAway("lion", "lison"))
