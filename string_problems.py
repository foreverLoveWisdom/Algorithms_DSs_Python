def is_palindrome(str):
    """
    Check if a string is a palindrome or not.
    string -> string
    "racecar" -> True
    "abc" -> False
    """
    chars = list(str)
    copied_chars = chars.copy()
    copied_chars.reverse()

    if copied_chars == chars:
        return True
    else:
        return False


def convert_strings_to_integers(str):
    """
    convert strings to integers without using int built-in function
    strings -> integers
    "123" -> 123
    "000" -> 0
    """
    # build a hash table to convert string to integers
    # convert strings into array of chars
    # reverse the array
    # use dispositional definitions of decimal number
    # add values together
    # return the sum

    number_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                   '6': 6, '7': 7, '8': 8, '9': 9}
    chars = list(str)
    sum = 0

    for idx, val in enumerate(reversed(chars)):
        num = number_dict.get(val)
        sum += num * (10**idx)

    return sum


def convert_integers_to_strings(number):
    """
    Convert an integer to a string
    int   -> string
    123   -> "123"
    0     -> "0"
    99999 -> "9999"
    """
    # get each digit in the number by using a loop, modulus, and division
    # operators.
    # Then using a hash table for looking up.
    # Then use a temporary array to store each char.
    # Finally join them in a reverse way.
    # Pay attention to special cases: 0, negative number,
    # and really big number.

    # if number == 0 or number == -0:
    #     return '0'
    # else:
    #     negative = False
    #     if number < 0:
    #         number *= -1
    #         negative = True
    #     temp_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
    #                  7: '7', 8: '8', 9: '9'}
    #     arr = []

    #     while(number > 0):
    #         temp_var = int(number % 10)
    #         arr.append(temp_dict.get(temp_var))
    #         number = int(number / 10)

    # if negative:
    #     return('-' + ''.join(reversed(arr)))
    # else:
    #     return ''.join(reversed(arr))
    # Will return wrong result if the number is too big because of the int
    # function

    is_negative = False

    if number < 0:
        number, is_negative = -number, True

    first_str = ord('0')
    s = []

    while True:
        s.append(chr(first_str + number % 10))
        number //= 10
        if number == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))
