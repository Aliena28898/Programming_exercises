'''
The Prime ant (A293689) is an obstinate animal that navigates the integers and divides them until there are only primes left, according to the following procedure:

An infinite list A is initialized to contain all the integers greater than 1: [2, 3, 4, 5, 6, …].

Let p be the position of the ant on the list. Initially p = 0, so the ant is at A[0] = 2.

At each turn, the ant moves as follows:

If A[p] is prime, move the ant one position forward, so p ← p + 1.

Otherwise (if A[p] is composite), let q be its smallest divisor greater than 1.

Replace A[p] with A[p] / q. Replace A[p−1] with A[p−1] + q.

Move the ant one position backward, so p ← p − 1.

Your task is to write the function prime_ant(n) that computes the position of the prime ant after n turns;

E.g

prime_ant(47)
   # => 9
'''   


#SOLUTION:
def is_prime(num):
    if num == 2:
        return 0
    else:
        for i in range(2,num):
            if (num%i==0):
                return i
        return 0

def prime_ant(n):
    li = list(range(2, 10000))#not infinite but good enough
    index = 0
    
    for t in range(0, n):
        if is_prime(li[index]) == 0:
            index += 1
        
        else:
            
            li[index-1] =  int(li[index-1] + is_prime(li[index]))
            li[index] = int(li[index]/is_prime(li[index]))
            index = index -1 
    
    return index


#TESTS:
# Basic tests

testc = [
    [28, 10],
    [11, 5],
    [19, 5],
    [2, 2],
    [12, 4],
    [29, 9],
    [46, 8],
]

for n, s in testc:
  soln = s
  test.assert_equals(prime_ant(n), soln, 'Wrong Value')
