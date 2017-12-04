'''
Given an array of 3 integers a, b and c, determine if they form a pythagorean triple.

A pythagorean triple is formed when:

c2 = a2 + b2

where c is the largest value of a, b, c.

For example: a = 3, b = 4, c = 5 forms a pythagorean triple, because 52 = 32 + 42

Return Values

1 if a, b and c form a pythagorean triple
0 if a, b and c do not form a pythagorean triple
For Python: return True or False
'''


#SOLUTION:
def pythagorean_triple(integers):
    a = integers[0]
    b = integers[1]
    c = integers[2]
    
    if a > b and a > c:
        return a*a == b*b+c*c
    if a < b and b > c:
        return b*b == a*a+c*c
    if c > b and a < c:
        return c*c == b*b+a*a
    else:
        pass


#TESTS:
test.assert_equals(pythagorean_triple([3, 4, 5]), True)
test.assert_equals(pythagorean_triple([3, 5, 9]), False)
