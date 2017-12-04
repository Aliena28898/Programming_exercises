'''Take debugging to a whole new level:

Given a string, remove every single bug.

This means you must remove all instances of the word 'bug' from within a given string, unless the word is plural ('bugs').

For example, given 'obugobugobuoobugsoo', you should return 'ooobuoobugsoo'.

Another example: given 'obbugugo', you should return 'obugo'.

Note that all characters will be lowercase.

Happy squishing!'''



#SOLUTION:

def debug(s):
    s = s.replace('bugs', '$pluralirnotreplaced!')
    s = s.replace('bug', '')
    s = s.replace('$pluralirnotreplaced!', 'bugs')
    return s
    
    
#TESTS:
test.assert_equals(debug('bug'), '')
test.assert_equals(debug('obugobugobuoobugsoo'), 'ooobuoobugsoo')
test.assert_equals(debug('obbugugo'), 'obugo')
test.assert_equals(debug('bugs bunny'), 'bugs bunny')
test.assert_equals(debug('bugs buggy'), 'bugs gy')
