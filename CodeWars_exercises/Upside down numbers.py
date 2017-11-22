"""
Consider the numbers 6969 and 9116. When you rotate them 180 degrees (upside down), these numbers remain the same. To clarify, if we write them down on a paper and turn the paper upside down, the numbers will be the same. Try it and see! Some numbers such as 2 or 5 don't yield numbers when rotated.

Given a range, return the count of upside down numbers within that range. For example, solve(0,10) = 3, because there are only 3 upside down numbers >= 0 and < 10. They are 0, 1, 8.

More examples in the test cases.

Good luck!
"""

#SOLUTION:

def solve(a, b):
    total = 0
    trans = {ord('9'):"6", ord('6'):"9"}
    for i in range(a, b):
        if i < 10:
            if i == 1 or i == 8 or i == 0:
                total += 1
            else:
                pass
        else:
            if str(i).translate(trans) == str(i)[::-1] and "2" not in str(i) and "3" not in str(i) and "4" not in str(i) and "5" not in str(i) and "7" not in str(i):
                total += 1
            else:
                pass
            
    return total

#TESTS:

Test.it("Basic tests")
Test.assert_equals(solve(0,10),3)
Test.assert_equals(solve(10,100),4)
Test.assert_equals(solve(100,1000),12)
Test.assert_equals(solve(1000,10000),20)
Test.assert_equals(solve(10000,15000),6)
Test.assert_equals(solve(15000,20000),9)
Test.assert_equals(solve(60000,70000),15)
Test.assert_equals(solve(60000,130000),55)
