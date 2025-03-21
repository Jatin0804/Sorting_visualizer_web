from .base import BaseSort

class SelectionSort(BaseSort):
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.increment_comparisons()
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                self.increment_swaps()
                self.add_step(arr)
        return self.get_stats() 