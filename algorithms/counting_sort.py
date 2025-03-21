from .base import BaseSort

class CountingSort(BaseSort):
    def sort(self, arr):
        if not arr:
            return self.get_stats()

        # Find the range of input array
        max_val = max(arr)
        min_val = min(arr)
        range_val = max_val - min_val + 1

        # Create count array and output array
        count = [0] * range_val
        output = [0] * len(arr)

        # Store count of each character
        for i in range(len(arr)):
            count[arr[i] - min_val] += 1
            self.increment_comparisons()

        # Change count[i] so that count[i] contains actual position of this element in output array
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # Build the output array
        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i] - min_val] - 1] = arr[i]
            count[arr[i] - min_val] -= 1
            self.increment_swaps()
            self.add_step(output.copy())

        # Copy the output array to arr, so that arr now contains sorted numbers
        for i in range(len(arr)):
            arr[i] = output[i]
            self.add_step(arr)

        return self.get_stats() 