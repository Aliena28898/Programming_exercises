"""
Finish the solution so that it takes an input n (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.

Assume: 0 <= n < 1000000000

Examples

       1  ->           "1"
      10  ->          "10"
     100  ->         "100"
    1000  ->       "1,000"
   10000  ->      "10,000"
  100000  ->     "100,000"
 1000000  ->   "1,000,000"
35235235  ->  "35,235,235"
"""

#SOLUTION:

def group_by_commas(n):
    s = ""
    num = str(n)[::-1]
    count = 0
    for i in num:
        s = s + i
        count += 1
        if count == 3:
            s = s + ","
            count = 0
    return s[::-1].strip(",")

#TESTS:

test.assert_equals(group_by_commas(1), '1')
test.assert_equals(group_by_commas(10), '10')
test.assert_equals(group_by_commas(100), '100')
test.assert_equals(group_by_commas(1000), '1,000')
test.assert_equals(group_by_commas(10000), '10,000')
test.assert_equals(group_by_commas(100000), '100,000')
test.assert_equals(group_by_commas(1000000), '1,000,000')
test.assert_equals(group_by_commas(35235235), '35,235,235')
