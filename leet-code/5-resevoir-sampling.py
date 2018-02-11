#!/usr/local/bin/python3

# Resevoir Sampling
#
# This is a good way to randomly select a series of data
# in which you must randomly select one but you don't
# know how long the data stream may be

# Question:
# Given a singly linked list, return a random node's value
# from the linked list. Each node must have the same probability
# of being chosen.
#
# Reference:
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getRandom(head):

    answer = head
    trace = head.next
    
    # n is used to track the probability
    n = 1

    while trace: 
        # After every iteration, we need to adjust
        # the proability such that all values that
        # have been read so far have an equal chance       
        if random.randint(0, n) == 0:
            answer = trace
        trace = trace.next
        n += 1

    return answer    
