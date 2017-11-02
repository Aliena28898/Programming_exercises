def values(n):
    import math
    solution = []

    def is_palindrome(value):
        return str(value) == str(value)[ ::-1 ]



    index = int(math.sqrt(n))

    while index > 0:
        factor = index
        index -= 1
        provisional = 0
        while factor > 0 and provisional < n:
            provisional = provisional + factor * factor


            if is_palindrome(provisional) and provisional != factor * factor and provisional < n and provisional not in solution:
                solution.append(provisional)

            else:
                pass

            factor -= 1

    return len(solution)

print(values(1000000))


def solve(n):
    index = 0
    prime_digits = [ '2', '3', '5', '7' ]

    def is_prime(num):
        for divisor in range(2, num - 1):

            if num % divisor == 0 and num != divisor:
                return False

        return True

    def is_valid(num):
        valid = True

        for element in str(num):
            if element in prime_digits:
                valid = False

        if valid == True:
            if is_prime(num):
                return True
            else:
                return False

        else:
            return False

    numb = 1
    while True:
        if is_valid(numb):
            index += 1
        else:
            pass

        if index == n:
            break

        numb += 1

    return numb

print(solve(10))


def solution(n):


    def convert_thousands(n):
        digit = int(str(n)[ len(str(n)) - 4 ])
        assert (1 <= digit <= 3)
        return "M" * digit

    def convert_hundreds(n):
        digit = int(str(n)[ len(str(n)) - 3 ])

        roman = {0: "", 1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}

        return roman[ digit ]

    def convert_decens(n):
        digit = int(str(n)[ len(str(n)) - 2 ])

        roman = {0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}

        return roman[ digit ]

    def convert_units(n):

        digit = int(str(n)[ len(str(n)) - 1 ])

        roman = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}

        return roman[ digit ]

    if len(str(n)) == 4:
        total_roman = convert_thousands(n)+convert_hundreds(n)+convert_decens(n)+convert_units(n)
    elif len(str(n)) == 3:
        total_roman = convert_hundreds(n)+convert_decens(n)+convert_units(n)
    elif len(str(n)) == 2:
        total_roman = convert_decens(n)+convert_units(n)
    else:
        total_roman = convert_units(n)

    return total_roman.

print(solution(12))