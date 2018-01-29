#/opt/bin/python

"""
QUICK SORT

This script implements the quicksort algorithm.

Quicksort requires the 'partition' method, which is described below.
(Merge sort requires the 'merge' method).

Time Complexity:
    O(n * log(n))

    Worst case: O(n^2), depending on how the pivots are chosen

    Note that in the general case, this algorithm works on average, better
    than mergesort and does it in a space efficient manner (in-place).

Space Complexity:
    O(n)
"""

def partition(array, left, right):
    """ Partition the array

    Inputs: (1) [LIST] List to sort
            (2) [INTEGER] Left most index of the list
            (3) [INTEGER] Rigth most index of the list

    Outputs: [INTEGER] Index of the pivot

    Description:
        This method picks the right most value as the 'pivot'.
        It then moves every value that is less than or equal to the
        pivot the left of the pivot and everythin that is greater
        to the right of the pivot.

        It will return the correct place of where the pivot should be.
    """

    pivot = array[right]

    leftMark = 0
    rightMark = right - 1

    done = False
    while done == False:

        # Traverse right until a swap candidate is found
        while leftMark <= rightMark and array[leftMark] <= pivot:
            leftMark += 1

        # Traverse left until a swap candidate is found
        while rightMark >= leftMark and array[rightMark] >= pivot:
            rightMark -= 1

        if leftMark > rightMark:
            done = True
        else:
            # Swap left & right marks
            array[leftMark], array[rightMark] = array[rightMark], array[leftMark]

    # Put the pivot in the rightful place
    # Which is where the "Left Marker" is
    array[leftMark], array[right] = array[right], array[leftMark]

    return leftMark

def quicksort(array, left, right):
    """ The Quicksort Algorithm

    Inputs: (1) [LIST] List to be sorted
            (2) [INTEGER] Left most index (typically: 0)
            (3) [INTEGER] Right most index (typically: len(array)-1

    Outputs: [LIST] Sorted list

    Description:
        The main algorithm after implementing partition.

        (1) Base Case: When the 'left' is greater than 'right'
                       --> Return the array
        (2) Partition
        (3) Call quicksort on left half
        (4) Call quicksort on right half
    """

    if left > right:
        return array

    partitionIndex = partition(array, left, right)

    quicksort(array, left, partitionIndex-1)
    quicksort(array, partitionIndex+1, right)

    return array

# ========== TESTING ==========
array = [1,7,3,5,9,2,4,8]
print(quicksort(array, 0, len(array)-1))
