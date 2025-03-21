from .base import BaseSort
import random

class QuickSort(BaseSort):
    def __init__(self):
        super().__init__()
        self.complexity = {
            'best': 'O(n log n)',
            'average': 'O(n log n)',
            'worst': 'O(n²)',
            'space': 'O(log n)'
        }

    def partition(self, arr, low, high):
        # Choose random pivot
        pivot_idx = random.randint(low, high)
        pivot = arr[pivot_idx]
        
        # Move pivot to end
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        self.increment_swaps()
        self.add_step(arr)
        
        i = low - 1
        
        for j in range(low, high):
            self.increment_comparisons()
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.increment_swaps()
                self.add_step(arr)
        
        # Move pivot to its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.increment_swaps()
        self.add_step(arr)
        
        return i + 1

    def quick_sort_helper(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort_helper(arr, low, pi - 1)
            self.quick_sort_helper(arr, pi + 1, high)

    def sort(self, arr):
        self.quick_sort_helper(arr, 0, len(arr) - 1)
        return self.get_stats() 