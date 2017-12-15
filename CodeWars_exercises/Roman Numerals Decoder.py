'''
https://www.codewars.com/kata/roman-numerals-decoder

Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:

solution('XXI') # should return 21
Courtesy of rosettacode.org

'''

#SOLUTION:
sol = 0
index = 0

def decode(roman, char, decimal):
    global sol
    global index
    if char in roman and decimal != 1:
        while  index < len(roman) and roman[index] == char:
          sol = sol + decimal
          index += 1
      
        if roman[index:].find(char) != -1:
            if char in "MCX":
                 sol = sol + int(decimal * 0.9)  
            else:
                sol = sol + int(decimal * 0.8)
              
            index = index + 2
    
    else:
        while index < len(roman) and roman[index] == char:
            sol = sol + decimal
            index += 1

def solution(roman): 
    global sol
    global index
    
    sol = 0
    index = 0

    decode(roman, 'M', 1000)
    decode(roman, 'D', 500)
    decode(roman, 'C', 100)
    decode(roman, 'L', 50)
    decode(roman, 'X', 10)
    decode(roman, 'V', 5)
    decode(roman, 'I', 1)
    
    return sol
      
      

#SAMPLE TESTS:
test.assert_equals(solution('XXI'), 21)
test.assert_equals(solution('MCMXC'), 1990)
test.assert_equals(solution('MMVIII'), 2008)
test.assert_equals(solution('MDCLXVI'), 1666)
test.assert_equals(solution('II'), 2)

