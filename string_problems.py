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
    "123" -> 123
    "000" -> 0
    """
    # build a hash table to convert string to integers
    # convert strings into array of chars
    # loop through strings from the back
    # use dispositional definitions of value
    # add values together
    # return integer

    number_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                   '6': 6, '7': 7, '8': 8, '9': 9}
    chars = list(str)
    sum = 0

    for idx, val in enumerate(reversed(chars)):
        num = number_dict.get(val)
        sum += num * (10**idx)

    return sum
