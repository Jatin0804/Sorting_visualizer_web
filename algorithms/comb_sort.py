from .base import BaseSort

class CombSort(BaseSort):
    def get_next_gap(self, gap):
        gap = (gap * 10) // 13
        if gap < 1:
            return 1
        return gap

    def sort(self, arr):
        n = len(arr)
        gap = n
        swapped = True

        while gap != 1 or swapped:
            gap = self.get_next_gap(gap)
            swapped = False

            for i in range(0, n - gap):
                self.increment_comparisons()
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    self.increment_swaps()
                    self.add_step(arr)
                    swapped = True

        return self.get_stats() 