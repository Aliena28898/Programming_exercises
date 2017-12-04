'''
Just for laugh Write a function that always return 5

Sounds easy right?? just bear in mind that you can't use any character among: 0123456789*+-/

Good luck :)
'''


#SOLUTION:
def unusual_five():
    array = ["f","i","v","e","lol"]
    return len(array)
    
    
#TESTS:
test.assert_equals( unusual_five(), 5)
