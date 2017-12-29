'''
Given an array of positive or negative integers

I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C# or C++ and as an array of arrays in other languages.

Example:

I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes: It can happen that a sum is 0 if some numbers are negative!

Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.
'''


#SOLUTION
prime_fact = []
import math
def is_prime(number):
    if number in [2, 3]:
        return True
    for i in range(2, number-1):
        if number % i == 0:
            return False
        i += 1
    return True

def find_prime_factors(number):
    global prime_fact
    lst = []
    for i in range(2, int(math.fabs(number))+1):
        print(i)
        if number % i == 0 and is_prime(i):
            lst.append(i)
            if i not in prime_fact:
                prime_fact.append(i)
                prime_fact.sort()
        i += 1
    
    return [number, lst]

def sum_for_list(lst):
    global prime_fact
    prime_fact = []
    for i in range(0, len(lst)):
        lst[i] = find_prime_factors(lst[i])
    
    for i in range(0, len(prime_fact)):
        sum = [prime_fact[i], 0]
        for element in lst:
            if prime_fact[i] in element[1]:
                sum[1] = sum[1] + element[0]
        prime_fact[i] = sum
    
    return prime_fact
        
        
