from .base import BaseSort

class InsertionSort(BaseSort):
    def __init__(self):
        super().__init__()
        self.complexity = {
            'best': 'O(n)',
            'average': 'O(n²)',
            'worst': 'O(n²)',
            'space': 'O(1)'
        }
    
    def sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and self.compare(key, arr[j]):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            self.add_step(arr)
        return self.get_stats() 