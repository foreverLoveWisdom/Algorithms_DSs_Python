"""

"""


def mergesort(arr):
    """
        Input: Unsorted Array.
        Output: Sorted Array.
        [1, 2, 6, 9, -5, 3] => [-5, 1, 2, 3, 6, 9]

        * Key idea:
        1. Combining two ordered arrays to make one large ordered array
        2. This operation immediately leads to a
        simple recursive sort method known as mergesort.

        * Pseduocode:
        1. Divide an array into 2 halves, sort the 2 halves
        (recursively)
        2. Then, merge the results.

        * Pros:
        One of the most attractive properties is that it guarantees to
        sort any array of N items in time proportional to NlogN.

        * Cons:
        Its prime disadvantage is that it uses extra space proportional
        to N.

        * Time complexity:
        Best case: O(n*logn)
        Average case: O(n*logn)
        Worst case: O(n*logn)

        * Space complexity: O(n)
        """
    if len(arr) > 1:
        middle = int(len(arr) / 2)

        left_arr = arr[:middle]
        right_arr = arr[middle:]

        mergesort(left_arr)
        mergesort(right_arr)

        left_index = 0
        right_index = 0
        current_index = 0

        # compare each index of the subarrays adding
        # the lowest value to the current_index
        while left_index < len(left_arr) and right_index < len(right_arr):
            if left_arr[left_index] < right_arr[right_index]:
                arr[current_index] = left_arr[left_index]
                left_index += 1
            else:
                arr[current_index] = right_arr[right_index]
                right_index += 1

            current_index += 1

        # copy remaining elements of left_array[] if any

        while left_index < len(left_arr):
            arr[current_index] = left_arr[left_index]
            left_index += 1
            current_index += 1

        # copy remaining elements of right_array[] if any
        while right_index < len(right_arr):
            arr[current_index] = right_arr[right_index]
            right_index += 1
            current_index += 1

        return arr


print(mergesort([5, 6, 7, 1, 2, 3]))
