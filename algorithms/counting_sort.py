from .base import BaseSort

class CountingSort(BaseSort):
    def __init__(self):
        super().__init__()
        self.complexity = {
            'best': 'O(n + k)',
            'average': 'O(n + k)',
            'worst': 'O(n + k)',
            'space': 'O(k)'
        }
    
    def sort(self, arr):
        if not arr:
            return self.get_stats()
            
        max_val = max(arr)
        count = [0] * (max_val + 1)
        
        for num in arr:
            count[num] += 1
            
        for i in range(1, len(count)):
            count[i] += count[i - 1]
            
        output = [0] * len(arr)
        
        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i]] - 1] = arr[i]
            count[arr[i]] -= 1
            
        for i in range(len(arr)):
            arr[i] = output[i]
            self.add_step(arr)
            
        return self.get_stats() 