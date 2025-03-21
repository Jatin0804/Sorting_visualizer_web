from .base import BaseSort

class HeapSort(BaseSort):
    def __init__(self):
        super().__init__()
        self.complexity = {
            'best': 'O(n log n)',
            'average': 'O(n log n)',
            'worst': 'O(n log n)',
            'space': 'O(1)'
        }
    
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and self.compare(arr[largest], arr[left]):
            largest = left
            
        if right < n and self.compare(arr[largest], arr[right]):
            largest = right
            
        if largest != i:
            self.swap(arr, i, largest)
            self.heapify(arr, n, largest)
    
    def sort(self, arr):
        n = len(arr)
        
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
            self.add_step(arr)
            
        for i in range(n - 1, 0, -1):
            self.swap(arr, 0, i)
            self.heapify(arr, i, 0)
            self.add_step(arr)
            
        return self.get_stats() 