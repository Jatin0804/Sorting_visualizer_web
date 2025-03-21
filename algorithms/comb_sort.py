from .base import BaseSort

class CombSort(BaseSort):
    def __init__(self):
        super().__init__()
        self.complexity = {
            'best': 'O(n log n)',
            'average': 'O(n²)',
            'worst': 'O(n²)',
            'space': 'O(1)'
        }
    
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
                if self.compare(arr[i + gap], arr[i]):
                    self.swap(arr, i, i + gap)
                    swapped = True
                self.add_step(arr)
        return self.get_stats() 