def alphabet_position(text):
    solution = ""

    for character in text:
        if character.isalpha():
            minus = str.lower(character)
            code = ord(minus)
            position = code - (ord('a')-1)

            solution = solution + " " + str(position)

    return solution.strip()



print(alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")