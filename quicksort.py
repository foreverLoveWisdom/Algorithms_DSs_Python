"""
    * General Overview: Why? How?
        * This algo is probably used more widely than any other.
        * Not difficult to implement.
        * Works well for a variety of different kinds of input data.
        * Substantially faster than any other sorting method in
            typical application.
        * It is in-place (uses only a small auxiliary stack)
        * Requires time proportioanl NlogN on average.
            => O(1) for space complexity and NlogN for time complexity.
        * Has a shorter inner loop than most other sorting algos
         => Fast in practice and in theory.
        * Main drawback:
            * Bad implementation => Quadratic Time Complexity: O(n^2)
            * However, there are optimization strategies to avoid this.

    * Pseudocode:
        * Like Merge Sort, QuickSort is a divide and conquer algorithm.
        * It picks an element as pivot and partitions the given array
            around the picked pivot. There are many different versions of

                * Quick Sort that pick pivot in different ways:
                1. Always pick first element as pivot.
                2. Always pick last element as pivot.
                3. Pick a random element as pivot.
                4. Pick median as pivot.

    * The key process in QuickSort is partition.
    * Target of partition is, given array and an element x of array as pivot,
    * put x at its correct position in sorted array and
    * put all smaller elements (smaller than x) before x, and
    * put all elements (greater than x) after x.
    * All this should be done in linear time.

    * Pseudocode:
    /* low  --> Starting index,  high  --> Ending index */
    quickSort(arr[], low, high)
    {
        if (low < high)
        {
            /* pi is partitioning index, arr[p] is now
            at right place */
            pi = partition(arr, low, high);

            quickSort(arr, low, pi - 1);  // Before pi
            quickSort(arr, pi + 1, high); // After pi
        }
    }
"""


def quicksort(arr):
    if arr:  # if given list (or tuple) with one ordered item or more:
        pivot = arr[0]

        # below will be less than:
        below = [i for i in arr[1:] if i < pivot]

        # above will be greater than or equal to:
        above = [i for i in arr[1:] if i >= pivot]

        return quicksort(below) + [pivot] + quicksort(above)
    else:
        return arr  # empty list


print(quicksort([1, 2, 3, -3, -2, -3, -1]))
