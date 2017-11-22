"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

#SOLUTION:

def find_it(seq):
    for num in seq:
        if seq.count(num)%2 == 0:
            pass
        else:
            return num

#TESTS:

test.describe("Example")
test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
test.assert_equals(find_it([8,8,45,45,6,6,54,54,54]), 54)
