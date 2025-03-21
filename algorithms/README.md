# Sorting Algorithms

This directory contains implementations of various sorting algorithms. Each algorithm is implemented as a class that inherits from `BaseSort`, providing consistent behavior and visualization capabilities.

## Base Class

The `BaseSort` class provides common functionality for all sorting algorithms:
- Step tracking for visualization
- Comparison and swap counting
- Time complexity information
- Common utility methods

## Implemented Algorithms

### 1. Bubble Sort (`bubble_sort.py`)
- Simple comparison-based algorithm
- Repeatedly steps through the list
- Swaps adjacent elements if they are in wrong order
- Time Complexity: O(n²)

### 2. Selection Sort (`selection_sort.py`)
- In-place comparison sorting
- Divides list into sorted and unsorted regions
- Repeatedly selects minimum element
- Time Complexity: O(n²)

### 3. Insertion Sort (`insertion_sort.py`)
- Builds sorted array one item at a time
- Efficient for small data sets
- Adaptive for nearly sorted data
- Time Complexity: O(n²)

### 4. Bogo Sort (`bogo_sort.py`)
- Randomly shuffles array until sorted
- Highly inefficient
- Used for educational purposes
- Time Complexity: O((n+1)!)

### 5. Comb Sort (`comb_sort.py`)
- Improvement over bubble sort
- Uses gap sequence
- Eliminates small values at end
- Time Complexity: O(n²)

### 6. Counting Sort (`counting_sort.py`)
- Non-comparison based sorting
- Works with integer keys
- Counts occurrences of elements
- Time Complexity: O(n + k)

### 7. Heap Sort (`heap_sort.py`)
- Comparison-based sorting
- Uses binary heap data structure
- In-place sorting
- Time Complexity: O(n log n)

### 8. Merge Sort (`merge_sort.py`)
- Divide and conquer algorithm
- Stable sorting algorithm
- Recursive implementation
- Time Complexity: O(n log n)

### 9. Quick Sort (`quick_sort.py`)
- Efficient, in-place sorting
- Uses pivot element
- Recursive implementation
- Time Complexity: O(n log n)

### 10. Radix Sort (`radix_sort.py`)
- Non-comparative sorting
- Works with integer keys
- Digit by digit sorting
- Time Complexity: O(d(n + k))

### 11. Shell Sort (`shell_sort.py`)
- Improvement over insertion sort
- Uses gap sequence
- Allows exchange of far apart elements
- Time Complexity: O(n log n)

### 12. Tim Sort (`tim_sort.py`)
- Hybrid sorting algorithm
- Combines merge sort and insertion sort
- Optimized for real-world data
- Time Complexity: O(n log n)

### 13. Gnome Sort (`gnome_sort.py`)
- Similar to insertion sort
- Uses series of swaps
- Simple implementation
- Time Complexity: O(n²)

### 14. Cocktail Sort (`cocktail_sort.py`)
- Bidirectional bubble sort
- Alternates direction of traversal
- Improves bubble sort performance
- Time Complexity: O(n²)

## Usage

Each algorithm can be used independently:

```python
from algorithms import BubbleSort

# Create an instance of the sorting algorithm
sorter = BubbleSort()

# Sort an array
array = [64, 34, 25, 12, 22, 11, 90]
result = sorter.sort(array)

# Get sorting statistics
print(f"Comparisons: {result['comparisons']}")
print(f"Swaps: {result['swaps']}")
print(f"Steps: {len(result['steps'])}")
```

## Adding New Algorithms

To add a new sorting algorithm:

1. Create a new file in this directory
2. Create a class that inherits from `BaseSort`
3. Implement the `sort` method
4. Set the complexity information in `__init__`
5. Use the base class methods for comparisons and swaps
6. Add steps for visualization

Example:
```python
from .base import BaseSort

class NewSort(BaseSort):
    def __init__(self):
        super().__init__()
        self.complexity = {
            'best': 'O(n)',
            'average': 'O(n log n)',
            'worst': 'O(n²)',
            'space': 'O(1)'
        }
    
    def sort(self, arr):
        # Implementation here
        return self.get_stats() 