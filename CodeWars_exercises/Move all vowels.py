"""
Given a string as input, move all of its vowels to the end of the string, in the same order as they were before.

Vowels are (in this kata): a, e, i, o, u

Note: all provided input strings are lowercase.

Examples

"day"    ==>  "dya"
"apple"  ==>  "pplae"
"""

#SOLUTION:

def move_vowels(input): 
    v = ""
    c = ""
    for l in input:
        if l in "aeiou":
            v = v + l
        else:
            c = c + l
    return c + v

#TESTS:

Test.assert_equals(move_vowels('day'), 'dya')
Test.assert_equals(move_vowels('apple'), 'pplae')
Test.assert_equals(move_vowels('peace'), 'pceae')
Test.assert_equals(move_vowels('maker'), 'mkrae')
