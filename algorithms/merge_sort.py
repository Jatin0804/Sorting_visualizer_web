from .base import BaseSort

class MergeSort(BaseSort):
    def __init__(self):
        super().__init__()
        self.complexity = {
            'best': 'O(n log n)',
            'average': 'O(n log n)',
            'worst': 'O(n log n)',
            'space': 'O(n)'
        }
    
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
    
    def merge_sort_helper(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort_helper(arr, left, mid)
            self.merge_sort_helper(arr, mid + 1, right)
            self.merge(arr, left, mid, right)
    
    def sort(self, arr):
        self.merge_sort_helper(arr, 0, len(arr) - 1)
        return self.get_stats() 