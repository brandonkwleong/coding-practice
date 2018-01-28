#/opt/bin/python

def lengthOfLongestSubstring(s):
    """
    Inputs: (1) [STRING] s
                String to check for the longest non-repeating substring
    
    Outupts: [NUMBER] Length of the longest non-repeating substring
    """
    
    lstr = list(s)
        
    # ----- Special Cases -----
    # Null or Blank String
    if not s:
        return 0
    
    # Only 1 character
    if len(lstr) == 1:
        return 1
        
    # ----- Begin Algorithm -----
    L = 0
    R = 1
    maxLength = 1
    savedIndexes = {}
    
    savedIndexes[lstr[L]] = L
    while R < len(s):
        
        if lstr[R] in s[L:R]:
            L = savedIndexes[lstr[R]] + 1

        savedIndexes[lstr[R]] = R
            
        if (R-L) + 1 > maxLength:
            maxLength = (R-L) + 1
            
        R += 1

    return maxLength
