import array_problems
import string_problems
import link_list


def test_palindrome_true():
    assert string_problems.is_palindrome("racecar") is True


def test_palindrome_false():
    assert string_problems.is_palindrome("123abc") is False


def test_str_to_integer():
    assert string_problems.convert_strings_to_integers("123") == 123
    assert string_problems.convert_strings_to_integers("000") == 0
    assert string_problems.convert_strings_to_integers("9999999111111111999999199999999119919191919191919191") == 9999999111111111999999199999999119919191919191919191


def test_integer_to_str():
    assert string_problems.convert_integers_to_strings(123) == "123"
    assert string_problems.convert_integers_to_strings(0) == "0"
    assert string_problems.convert_integers_to_strings(9999999111) == "9999999111"
    assert string_problems.convert_integers_to_strings(-123) == "-123"
    assert string_problems.convert_integers_to_strings(-1) == "-1"
    assert string_problems.convert_integers_to_strings(-999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999) == "-999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"


def test_list_node():
    assert link_list.ListNode() is not None
    linked_list = link_list.ListNode()
    assert linked_list.data == 0 and linked_list.next is None
