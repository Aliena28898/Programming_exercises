"""
Your task is to make a program takes in a sentence (without puncuation), adds all words to a list and returns the sentence as a string which is the positions of the word in the list. Casing should not matter too.

Example

"Ask not what your COUNTRY can do for you ASK WHAT YOU CAN DO FOR YOUR country"

becomes

"01234567802856734"

Another example

"the one bumble bee one bumble the bee"

becomes

"01231203"
"""

#SOLUTION:

def compress(sentence):
    lista = sentence.lower().split()
    sub = []
    output = ""
    for element in lista:
        if element in sub:
            output = output + str(sub.index(element))
        else:
            output = output + str(len(sub))
            sub.append(element)
            
    return output
    
#TESTS
    
test.assert_equals(compress("The bumble bee"), "012")
test.assert_equals(compress("the one bumble bee one bumble the bee"), "01231203")
test.assert_equals(compress("the one one bumble bee one bumble the bee"), "011231203")
