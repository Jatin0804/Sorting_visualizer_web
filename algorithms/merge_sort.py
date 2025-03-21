from .base import BaseSort

class MergeSort(BaseSort):
    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # Create temp arrays
        L = [0] * n1
        R = [0] * n2

        # Copy data to temp arrays
        for i in range(n1):
            L[i] = arr[l + i]
        for j in range(n2):
            R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr
        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            self.increment_comparisons()
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            self.increment_swaps()
            self.add_step(arr)

        # Copy the remaining elements of L[], if any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            self.increment_swaps()
            self.add_step(arr)

        # Copy the remaining elements of R[], if any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            self.increment_swaps()
            self.add_step(arr)

    def merge_sort_helper(self, arr, l, r):
        if l < r:
            m = (l + r) // 2
            self.merge_sort_helper(arr, l, m)
            self.merge_sort_helper(arr, m + 1, r)
            self.merge(arr, l, m, r)

    def sort(self, arr):
        self.merge_sort_helper(arr, 0, len(arr) - 1)
        return self.get_stats() 