import array_problems
import string_problems


def test_palindrome_true():
    assert string_problems.is_palindrome("racecar") is True


def test_palindrome_false():
    assert string_problems.is_palindrome("123abc") is False


def test_str_to_integer():
    assert string_problems.convert_strings_to_integers("123") == 123
    assert string_problems.convert_strings_to_integers("000") == 0
    assert string_problems.convert_strings_to_integers("9999999111") == 9999999111
