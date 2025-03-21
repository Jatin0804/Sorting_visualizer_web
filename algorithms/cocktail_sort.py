from .base import BaseSort

class CocktailSort(BaseSort):
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
        swapped = True
        start = 0
        end = n - 1
        
        while swapped:
            swapped = False
            
            # Forward pass
            for i in range(start, end):
                if self.compare(arr[i + 1], arr[i]):
                    self.swap(arr, i, i + 1)
                    swapped = True
                self.add_step(arr)
            
            if not swapped:
                break
                
            swapped = False
            end -= 1
            
            # Backward pass
            for i in range(end - 1, start - 1, -1):
                if self.compare(arr[i + 1], arr[i]):
                    self.swap(arr, i, i + 1)
                    swapped = True
                self.add_step(arr)
                
            start += 1
            
        return self.get_stats() 