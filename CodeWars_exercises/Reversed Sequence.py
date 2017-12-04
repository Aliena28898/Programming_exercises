'''
Get the number n to return the reversed sequence from n to 1.

Example : n=5 >> [5,4,3,2,1]
'''

#SOLUTION:
def reverse_seq(n):
    solution = [ ]
    for num in range(n, 0, -1):
        solution.append(num)

    return solution
    
    
#TESTS:
test.assert_equals(reverse_seq(5),[5,4,3,2,1])
