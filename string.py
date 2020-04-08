def check_palindrome(str):
    chars          = list(str)
    copied_chars   = chars.copy()
    copied_chars.reverse()

    if(copied_chars == chars):
        print("\nThis is PALINDROME.")
    else:
        print("\nThis is NOT palindrome.")

check_palindrome("racer")
