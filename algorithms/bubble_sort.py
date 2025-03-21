from .base import BaseSort

class BubbleSort(BaseSort):
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.increment_comparisons()
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.increment_swaps()
                    self.add_step(arr)
        return self.get_stats() 