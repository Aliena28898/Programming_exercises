'''
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)
'''


#SOLUTION:

def find_missing_letter(chars):
    last = ord(chars[0])-1
    for letter in chars:
        if last != ord(letter)-1:
            return chr(ord(letter)-1)
        else:
            last = ord(letter)
            
#TESTS:
test.describe("kata tests")
test.it("example tests")
test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')
