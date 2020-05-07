def find_max(data):
    """Return the maximum element from a nonempty Python list
    * Running time grows proportional to n => O(n)
    """
    biggest = data[0]  # initial value to beat

    for val in data:  # For each value:
        if val > biggest:  # If it is greater than the best so far,
            biggest = val  # We have ounf a new best(so far)

    return biggest  # When loop ends, biggest is the max


print(find_max([1, 2, 4, -2, -10, 5]))
