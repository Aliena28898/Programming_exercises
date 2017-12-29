'''
In this kata you have to implement a base converter, which converts positive integers between arbitrary bases / alphabets. Here are some pre-defined alphabets:

bin      = '01'
oct      = '01234567'
dec      = '0123456789'
hex      = '0123456789abcdef'
allow    = 'abcdefghijklmnopqrstuvwxyz'
allup    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
The function convert() should take an input (string), the source alphabet (string) and the target alphabet (string). You can assume that the input value always consists of characters from the source alphabet. You don't need to validate it.

Examples
convert("15", dec, bin)       ==>  "1111"
convert("15", dec, oct)       ==>  "17"
convert("1010", bin, dec)     ==>  "10"
convert("1010", bin, hex)     ==>  "a"
convert("0", dec, alpha)      ==>  "a"
convert("27", dec, allow)     ==>  "bb"
convert("hello", allow, hex)  ==>  "320048"

Additional Notes:

The maximum input value can always be encoded in a number without loss of precision in JavaScript. In Haskell, intermediate results will probably be too large for Int.
The function must work for any arbitrary alphabets, not only the pre-defined ones
You don't have to consider negative numbers
'''

```python
#SOLUTION:

def decode(input, source):
    input = input[::-1]
    index = 0
    result = 0
    while index < len(input):
        result = result + source.find(input[index]) * (len(source)**index)
        index = index + 1
    
    return result
    
    
    
def encode(number, target):
    result = []
    base = len(target)
    maxpower = 0
    if number < base:
            result.append(target[0])
    while number > 0:
        power = 0
        
        while base**power <= number:
            power += 1
        power -= 1    
        if power > maxpower:
            maxpower = power
            for i in range(0, maxpower+1):
                result.append(target[0])
        
        res = int(number/base**power)
        result[power] = target[res]
        
        number = number - base**power * res
    
        
    final = ""    
    for element in result:
        final = final + element
    return final[::-1]
    

def convert(input, source, target):
    number = decode(input, source)
    number = encode(number, target)
    
    return number
    
#TESTS:
test.it('should convert between numeral systems')
test.assert_equals(convert("15", dec, bin), '1111', '"15" dec -> bin');
test.assert_equals(convert("15", dec, oct), '17', '"15" dec -> oct');
test.assert_equals(convert("1", dec, oct), '1', '"1" dec -> oct');
test.assert_equals(convert("0", dec, oct), '0', '"0" dec -> oct');
test.assert_equals(convert("1010", bin, dec), '10', '"1010" bin -> dec');
test.assert_equals(convert("1010", bin, hex), 'a', '"1010" bin -> hex');

test.it('should convert between other bases')
test.assert_equals(convert("0", dec, alpha), 'a', '"0" dec -> alpha');
test.assert_equals(convert("27", dec, allow), 'bb', '"27" dec -> alpha_lower');
test.assert_equals(convert("hello", allow, hex), '320048', '"hello" alpha_lower -> hex')
test.assert_equals(convert("SAME", alup, alup), 'SAME', '"SAME" alpha_upper -> alpha_upper');
    
```
