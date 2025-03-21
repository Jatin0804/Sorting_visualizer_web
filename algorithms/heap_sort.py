from .base import BaseSort

class HeapSort(BaseSort):
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            self.increment_comparisons()
            if arr[left] > arr[largest]:
                largest = left

        if right < n:
            self.increment_comparisons()
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.increment_swaps()
            self.add_step(arr)
            self.heapify(arr, n, largest)

    def sort(self, arr):
        n = len(arr)

        # Build a maxheap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.increment_swaps()
            self.add_step(arr)
            self.heapify(arr, i, 0)

        return self.get_stats() 