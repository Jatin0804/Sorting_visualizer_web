from .base import BaseSort

class BubbleSort(BaseSort):
    def __init__(self):
        super().__init__()
        self.complexity = {
            'best': 'O(n)',
            'average': 'O(n²)',
            'worst': 'O(n²)',
            'space': 'O(1)'
        }
    
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                self.increment_comparisons()
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.increment_swaps()
                    swapped = True
                self.add_step(arr)
            if not swapped:
                break
        return self.get_stats() 