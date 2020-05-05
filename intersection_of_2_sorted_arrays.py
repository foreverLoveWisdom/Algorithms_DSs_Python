from bisect import bisect_left


def compute_intersection_of_2_sorted_arrays(arr1, arr2):
    """
    * Returns a new array contains elements in 2 sorted arrays
    (no duplicate values)
    * Input:
        1. [2, 3, 3, 5, 5, 6, 7, 7 ,8 ,12]
        2. [5, 5, 6, 8, 8, 9, 10, 10]
    * Output:
        [5, 6, 8]
    """
    # Time complexity: O(len1 * len2)
    # Space complexity: O(len1) or O(len2)
    result = []
    # len1 = len(arr1)
    # len2 = len(arr2)
    # if len1 > len2:
    #     for i in arr1:
    #         for j in arr2:
    #             if i == j:
    #                 if i not in result:
    #                     result.append(i)
    # else:
    #     for j in arr2:
    #         for i in arr1:
    #             if j == i:
    #                 if j not in result:
    #                     result.append(i)

    # Time Complexity: O(mlogn)
    # Space Complexity: O(n)
    def is_present(k):
        i = bisect_left(arr2, k)
        return i < len(arr2) and arr2[i] == k

    for index, value in enumerate(arr1):
        if (index == 0 or value != arr1[index - 1]) and is_present(value):
            result.append(value)

    return result


print(compute_intersection_of_2_sorted_arrays([1, 2, 3], [-3, -2, 0, 1, 2, 3]))
# print(help(compute_intersection_of_2_sorted_arrays))
