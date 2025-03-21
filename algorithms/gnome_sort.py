from .base import BaseSort

class GnomeSort(BaseSort):
    def sort(self, arr):
        n = len(arr)
        index = 0
        while index < n:
            if index == 0:
                index += 1
            self.increment_comparisons()
            if arr[index] >= arr[index - 1]:
                index += 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                self.increment_swaps()
                self.add_step(arr)
                index -= 1
        return self.get_stats() 