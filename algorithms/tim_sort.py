from .base import BaseSort

class TimSort(BaseSort):
    def __init__(self):
        super().__init__()
        self.complexity = {
            'best': 'O(n)',
            'average': 'O(n log n)',
            'worst': 'O(n log n)',
            'space': 'O(n)'
        }
    
    def insertion_sort(self, arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            
            while j >= left and self.compare(key, arr[j]):
                arr[j + 1] = arr[j]
                j -= 1
                self.add_step(arr)
                
            arr[j + 1] = key
            self.add_step(arr)
    
    def merge(self, arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < n1 and j < n2:
            if self.compare(R[j], L[i]):
                arr[k] = R[j]
                j += 1
            else:
                arr[k] = L[i]
                i += 1
            k += 1
            self.add_step(arr)
        
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            self.add_step(arr)
            
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            self.add_step(arr)
    
    def sort(self, arr):
        n = len(arr)
        min_run = 32
        
        for i in range(0, n, min_run):
            self.insertion_sort(arr, i, min((i + min_run - 1), n - 1))
            
        size = min_run
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min((left + size - 1), (n - 1))
                right = min((left + 2 * size - 1), (n - 1))
                
                if mid < n - 1:
                    self.merge(arr, left, mid, right)
                    
            size = 2 * size
            
        return self.get_stats() 