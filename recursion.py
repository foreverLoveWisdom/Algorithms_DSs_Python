"""
* Running-time analysis of recursive algorithms:

    - Account for each operation that is performed based upon the particular activation
        of the function that manages the flow of control
            at the time it is executed.
    
    - For each activation (stack frame), we only account for the number of operations
        that are performed within the body of that activation.

"""


def factorial(number):
    """Returns factorial

    Arguments:
        number {integer } -- [positive]

    Returns:
        [integer] -- [positive]
    """
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def factorial_loop(number):
    fact = 1

    for i in range(2, number + 1):
        fact *= i

    return fact


print(factorial(20))
print(factorial_loop(20))
