'''
How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc. Test examples:

rot13("EBG13 rknzcyr.") == "ROT13 example.";
rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"
'''


SOLUTION:

import string
def rot13(message):
    alpha = (string.ascii_lowercase+string.ascii_lowercase+string.ascii_uppercase+string.ascii_uppercase)
    mess = ""
    for c in message:
        if c not in string.ascii_letters:
            mess = mess + c
        else:
            mess = mess + alpha[alpha.index(c)+13]
      
           
    return mess
 
#TESTS:
test.expect(rot13("EBG13 rknzcyr.") == "ROT13 example.")
test.expect(rot13("V nz n ornhgvshy cbgngb.") == "I am a beautiful potato.") 
 
