'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''


#SOLUTION:
def solution(string,markers):
    assert(isinstance(string, str))
    for mark in markers:
        comment = False
        index = 0
        while index < len(string):
            if string[index:].startswith(mark) and not comment:
                comment = True
            if string[index] == '\n':
                comment = False
                while string[index-1] == " ":
                    string = string[:index-1] + string[index:]
                    index -=1
            if comment:
                string = string[:index]+string[index+1:]
                index -=1
            
            index += 1
    
    return string.strip(" ")
    
    
#TESTS:
Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
Test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
Test.assert_equals(solution("now     \n $you \n bring me$a sandwitch", ["@", "$"]), "now\n\n bring me")
