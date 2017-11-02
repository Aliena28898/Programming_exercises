def is_valid_IP(strng):
    def is_valid_number(number):
        return number[ 0 ] != "0" and 0 <= int(number) <= 255
    point_place = 0
    octets = 0
    while strng[point_place+1:].find(".") != -1:
        number = strng[point_place:strng.find(".")]
        point_place = strng[point_place + len(number):].find(".")
        if not is_valid_number(number):
            return False

        else:
            print(number)
            print("valid")
            octets = octets + 1

    if octets == 4:
        return True

    else:
        print(octets)
        return False

print(is_valid_IP('12.255.56.1'))