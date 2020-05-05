"""
* Insertion sort is a stable algorithm with poor performance.

* Insertion sort is used when number of elements is small.
    It can also be useful when input array is almost sorted,
        only few elements are misplaced in complete big array.
        
* 
"""


def insertion_sort(arr):
    """
        Input: Unsorted Array.
        Output: Sorted Array.
        [1, 2, 6, 9, -5, 3] => [-5, 1, 2, 3, 6, 9]

        * Key Idea:
        1. Insertion Sort consists of a while-loop nested in a for-loop.
        2. Loop through every value of the array starting
           with the first index. This is because
           we will be comparing each index with the previous index.

        * Pseudocode:
        1. Make space to insert the current item by
        moving larger items one position to the right before
        inserting the current item into the vacated position.

        2. The items to the left of the current index are
        in sorted order during the sort, but they are not
        in their final positions, because they may have to
        be moved to make rooms for smaller items
        encountered later.

        * Time Complexity:
        ** Best: O(n)
        ** Average: O(n^2)
        ** Worst: O(n^2)

        * Space Complexity: O(n)
        """
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


print(insertion_sort([5, 6, 7, 1, 2, 3]))
