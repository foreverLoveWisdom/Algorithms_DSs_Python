"""
Sorting is a common problem in computing. Sorting is used to preprocessing
the collection to make searching faster (binary search through an array)
as well as identify items that are similar (students are sorted
on test scores)

Naive sorting algo runs in O(n^2).
A number of sorting algorithms run in O(n*logn) time:
heapsort, merge sort, and quicksort.

Heapsort is in-place but not stable.
Merge sort is stable but not in-place.
Quicksort runs O(n^2) in worst case.

An in-place sort is one which uses O(1) space.
A stable sort is one where entries which
are equal appear in their original order.

A well-implemented quicksort is usually the best choice for sorting.

For short arrays, 10 or fewer elements, inserting sort
is easier to code and faster than asymtotically superior algorithm.
"""


class Example:
    def __init__(self, arr=[3, 10, 2, 5]):
        self.data = arr

    def selection_sort(self):
        """
        Space complexity: O(n)
        Time Complexity: O(n^2)
        """
        arr = self.data
        length = len(arr)

        for i in range(length):
            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, length):
                if arr[min_idx] > arr[j]:
                    min_idx = j

            # Swap the found minimum element with
            # the first element
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr

    def less(self, a, b):
        return a - b < 0

    def exchange_void(self, i, j):
        t = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = t
        return self.data

    def show(self):
        i = 0
        print("\nLength of data is: %s" % (len(self.data)))
        while i < len(self.data):
            print(self.data[i], end=" ")
            i += 1

    def is_sorted(self):
        arr_len = len(self.data)
        i = 1

        while i < arr_len:
            if self.less(self.data[i], self.data[i - 1]):
                return False
            i += 1

        return True


result = Example()
print(result.is_sorted())
print(result.data)
# print(result.exchange_void(1, 2))
# print(result.show())
print(result.selection_sort())
