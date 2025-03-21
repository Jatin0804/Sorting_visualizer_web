from .base import BaseSort

class InsertionSort(BaseSort):
    def sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0:
                self.increment_comparisons()
                if arr[j] > key:
                    arr[j + 1] = arr[j]
                    self.increment_swaps()
                    self.add_step(arr)
                    j -= 1
                else:
                    break
            arr[j + 1] = key
            self.add_step(arr)
        return self.get_stats() 