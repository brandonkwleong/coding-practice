#!/usr/local/bin/python3

# Question:
# Given a binary array, find the maximum length of a contiguous
# subarray with equal number of 0 and 1.

def maxLength(array):

    # Initialize 0 index as negative 1
    t = {0: -1}
    count = 0
    answer = 0

    for i, num in enumerate(array):

        # Decrement count if 0, increment if 1
        if num == 0:
            count -= 1
        else:
            count += 1

        # If the count is not saved, save it!
        if count not in t:
            t[count] = i

        # If the count is saved, then the distance between
        # the current index and the saved count is a viable
        # solution
        else:
            compare = i - t[count]
            if compare > answer:
                answer = compare

    return answer

# ===== Testing =====

a = [0,1,1,1,0,0,0]
print(maxLength(a))
