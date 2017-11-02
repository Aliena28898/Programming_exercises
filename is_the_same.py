def comp(array1, array2):
    if len(array1) != len(array2):
        return False

    else:
        for num in array1:
            square = num ** 2

            try:
                position = array2.index(square)
                print(array2.index(square))
                array2.remove(position)

            except ValueError:
                return False

        return True

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2) == True)

a3 = [121, 144, 19, 161, 19, 144, 19, 11]
a4 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a3, a4) == False)