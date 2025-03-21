from .base import BaseSort

class TimSort(BaseSort):
    def insertion_sort(self, arr, left, right):
        for i in range(left + 1, right + 1):
            temp = arr[i]
            j = i - 1

            # Move elements of arr[0..i-1], that are greater than temp,
            # to one position ahead of their current position
            while j >= left:
                self.increment_comparisons()
                if arr[j] > temp:
                    arr[j + 1] = arr[j]
                    self.increment_swaps()
                    self.add_step(arr)
                    j -= 1
                else:
                    break

            arr[j + 1] = temp
            self.add_step(arr)

    def merge(self, arr, l, m, r):
        # Original array is broken in two parts, left and right array
        len1, len2 = m - l + 1, r - m
        left, right = [], []
        for i in range(0, len1):
            left.append(arr[l + i])
        for i in range(0, len2):
            right.append(arr[m + 1 + i])

        i, j, k = 0, 0, l

        # After comparing, we merge those two array in larger sub array
        while i < len1 and j < len2:
            self.increment_comparisons()
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            self.increment_swaps()
            self.add_step(arr)

        # Copy remaining elements of left, if any
        while i < len1:
            arr[k] = left[i]
            k += 1
            i += 1
            self.increment_swaps()
            self.add_step(arr)

        # Copy remaining element of right, if any
        while j < len2:
            arr[k] = right[j]
            k += 1
            j += 1
            self.increment_swaps()
            self.add_step(arr)

    def sort(self, arr):
        n = len(arr)
        min_run = 32

        # Sort individual subarrays of size RUN
        for start in range(0, n, min_run):
            end = min(start + min_run - 1, n - 1)
            self.insertion_sort(arr, start, end)

        # Start merging from size RUN (or 32). It will merge to form size 64, then 128, 256 and so on
        size = min_run
        while size < n:
            # Pick starting point of left sub array. We are going to merge arr[left..left+size-1] and arr[left+size, left+2*size-1]
            for left in range(0, n, 2 * size):
                # Find ending point of left sub array mid+1 is starting point of right sub array
                mid = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), (n - 1))

                # Merge sub array arr[left.....mid] & arr[mid+1....right]
                if mid < n - 1:
                    self.merge(arr, left, mid, right)

            size = 2 * size

        return self.get_stats() 