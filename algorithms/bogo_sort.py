from .base import BaseSort
import random

class BogoSort(BaseSort):
    def is_sorted(self, arr):
        for i in range(len(arr) - 1):
            self.increment_comparisons()
            if arr[i] > arr[i + 1]:
                return False
        return True

    def shuffle(self, arr):
        for i in range(len(arr)):
            j = random.randint(0, len(arr) - 1)
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
                self.increment_swaps()
                self.add_step(arr)

    def sort(self, arr):
        while not self.is_sorted(arr):
            self.shuffle(arr)
        return self.get_stats() 