from .base import BaseSort

class RadixSort(BaseSort):
    def __init__(self):
        super().__init__()
        self.complexity = {
            'best': 'O(d(n + k))',
            'average': 'O(d(n + k))',
            'worst': 'O(d(n + k))',
            'space': 'O(n + k)'
        }
    
    def counting_sort_for_radix(self, arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        # Store count of occurrences in count[]
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1
            self.increment_comparisons()

        # Change count[i] so that count[i] contains actual position of this digit in output[]
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
            self.increment_swaps()
            self.add_step(output.copy())

        # Copy the output array to arr[], so that arr[] now contains sorted numbers according to current digit
        for i in range(n):
            arr[i] = output[i]
            self.add_step(arr)

    def sort(self, arr):
        if not arr:
            return self.get_stats()

        # Find the maximum number to know number of digits
        max1 = max(arr)

        # Do counting sort for every digit. Note that instead of passing digit number, exp is passed.
        # exp is 10^i where i is current digit number
        exp = 1
        while max1 // exp > 0:
            self.counting_sort_for_radix(arr, exp)
            exp *= 10

        return self.get_stats() 