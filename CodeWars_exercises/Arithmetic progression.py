'''
https://www.codewars.com/kata/arithmetic-progression

In your class, you have started lessons about arithmetic progression.
Since you are also a programmer, you have decided to write a function that will return the first 'n' elements of the sequence with the given common difference 'r' and first element 'a'. Result should be separated by comma and space.

Example:

arithmetic_sequence_elements(1, 2, 5) == '1, 3, 5, 7, 9'

'''


#SOLUTION:
def arithmetic_sequence_elements(a, r, n):
    solution = ""
    num = a
    for i in range (0, n):
        solution = solution+", "+str(num)
        num = num+r
    return solution.strip(", ");
    
    

#SAMPLE TESTS:
test.assert_equals(arithmetic_sequence_elements(1, 2, 5), '1, 3, 5, 7, 9')
test.assert_equals(arithmetic_sequence_elements(1, -3, 10), '1, -2, -5, -8, -11, -14, -17, -20, -23, -26')
