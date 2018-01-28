#/opt/bin/python
 
def lengthOfPalindrome(listStr, LI, RI):
    """
    Inputs: (1) [LIST] listStr
                This is a string that is converted into a list

            (2) [NUMBER] LI
                Left index of 'center' of a potential palindrome

            (3) [NUMBER] RI
                Right index of 'center' of a potential palindrome

    Output: [NUMBER]
            The output will be the length of the longest substring
            of the list string given, with LI & RI describing the 'center'
            to start with.
    """

    while LI >= 0 and RI < len(listStr) and listStr[LI] == listStr[RI]:
        LI -= 1
        RI += 1
        
    return (RI-LI) - 1
    
def longestPalindrome(s):
    """
    Inputs: (1) [STRING] s
                String to check for the longest palindrome inside

    Output: [STRING]
            The longest palindrome in the string given
    """

    listStr = list(s)

    # ----- Special Cases -----
    if not s:
        return ""
    
    if len(s) == 1:
        return s
    # -------------------------
    
    maxLength = 0
    startInd = 0
    endInd = 0
    
    for ind in xrange(len(listStr)):
        
        len1 = self.lengthOfPalindrome(listStr, ind, ind)
        len2 = self.lengthOfPalindrome(listStr, ind, ind+1)
        
        lenToUse = max(len1, len2)
        
        if lenToUse > maxLength:
            maxLength = lenToUse
            startInd = ind - (lenToUse - 1) / 2
            endInd = ind + lenToUse/2
    
    return ''.join(listStr[startInd:endInd+1])
