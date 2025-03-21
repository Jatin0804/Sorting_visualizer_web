from .base import BaseSort

class GnomeSort(BaseSort):
    def __init__(self):
        super().__init__()
        self.complexity = {
            'best': 'O(n)',
            'average': 'O(n²)',
            'worst': 'O(n²)',
            'space': 'O(1)'
        }
    
    def sort(self, arr):
        index = 0
        n = len(arr)
        
        while index < n:
            if index == 0:
                index += 1
                
            if self.compare(arr[index], arr[index - 1]):
                index += 1
            else:
                self.swap(arr, index, index - 1)
                index -= 1
                
            self.add_step(arr)
            
        return self.get_stats()