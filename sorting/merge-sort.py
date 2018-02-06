#/opt/bin/python

"""
MERGE SORT

This script is for practicing the implementation of merge sort.

Merge sort requires:
    1. A merge method -> merge
    2. It's own method to call itself -> mergesort

Time Complexity:
    O(n * log(n))

    n --> Merge requires O(n) time to merge the two lists as it
          needs to go through every element of the list

    log(n) --> Dividng the problem by half everytime

Space Complexity:
    O(n) + O(log(n)) => O(n)

    O(n) --> Need to store all the elements of the list
    O(log(n)) --> Counting the stack frames
"""

def merge(a1, a2):
    """ Merges two sorted lists into a single sorted list

    Inputs: (1) [LIST] List 1
            (2) [LIST] List 2

    Outputs: [LIST] A sorted list
    """

    t1 = 0
    t2 = 0

    rList = []
    while t1 < len(a1) or t2 < len(a2):

        # For mismatched sized lists, we've hit the len
        # of one list, append the other
        if t2 == len(a2):
            rList.append(a1[t1])
            t1 += 1

        elif t1 == len(a1):
            rList.append(a2[t2])
            t2 += 1

        # Comparing the list elements
        elif a1[t1] <= a2[t2]:
            rList.append(a1[t1])
            t1 += 1

        elif a2[t2] < a1[t1]:
            rList.append(a2[t2])
            t2 += 1

    return rList

def mergesort(list):
    """ The mergesort algorithm

    Input: [LIST] A list of numbers
    Output: [LIST] The sorted list

    Description:
        1. If list is a single element, return the list
        2. Break down the left side and right side of the list
        3. Merge the two lists
    """

    if not list:
        return []    

    if len(list) == 1:
        return list

    a1 = mergesort(list[0:int(len(list)/2)])
    a2 = mergesort(list[(int(len(list)/2)):len(list)])

    return merge(a1, a2)

# ========== TESTING ==========
list = [5,8,2,3,10,9,7]
print(mergesort(list))
