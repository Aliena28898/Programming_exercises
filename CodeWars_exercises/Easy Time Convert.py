'''
This challenge requires you to convert an integer. If the input is 78, then your program should output the string '01:18' because 78 minutes converts to 1 hour and 18 minutes. If the input is 0 or negative value, then your program should output the string '00:00'

We will use the modulo operation to solve this challenge. The modulo operation simply returns the remainder after a division, so for example, the remainder of 5 / 2 is 1, so the modulo of 5 / 2 is 1.

Good luck :D
'''

#SOLUTION:

def timeConvert(num):
    if num <= 0:
        return "00:00"
    else:
        if num/60 < 10:
            sol = "0" + str(int(num/60)) + ":" 
        else:
            sol = str(int(num/60)) + ":" 
        if num%60 < 10:
            sol = sol + "0" + str(int(num%60))
        else:
            sol = sol + str(int(num%60))
        return(sol)
        

#TESTS:

test.expect(timeConvert(0)=='00:00', 'Test at 0')
test.expect(timeConvert(-6)=='00:00', 'Negative number');
test.expect(timeConvert(8)=='00:08', '8 minutes');
test.expect(timeConvert(32)=='00:32', '32 minutes');
test.expect(timeConvert(75)=='01:15', 'over an hour');
test.expect(timeConvert(63)=='01:03', 'over an hour');
test.expect(timeConvert(134)=='02:14', 'over two hours');
test.expect(timeConvert(180)=='03:00', 'three hours');
test.expect(timeConvert(970)=='16:10', 'over 16 hours');
test.expect(timeConvert(565757)=='9429:17', 'big numbers');
