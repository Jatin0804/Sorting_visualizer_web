# Sorting Algorithm Visualizer

A web-based visualization tool for various sorting algorithms. This project helps users understand how different sorting algorithms work by providing a visual representation of the sorting process.

## Features

- Visual representation of sorting algorithms
- Real-time comparison and swap counting
- Adjustable sorting speed and array size
- Support for multiple sorting algorithms
- Time complexity information for each algorithm
- Responsive design for all screen sizes

## Supported Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity |
|-----------|-----------|--------------|------------|------------------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Bogo Sort | O(n) | O((n+1)!) | O(∞) | O(1) |
| Comb Sort | O(n log n) | O(n²) | O(n²) | O(1) |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Radix Sort | O(d(n + k)) | O(d(n + k)) | O(d(n + k)) | O(n + k) |
| Shell Sort | O(n log n) | O(n log n) | O(n²) | O(1) |
| Tim Sort | O(n) | O(n log n) | O(n log n) | O(n) |
| Gnome Sort | O(n) | O(n²) | O(n²) | O(1) |
| Cocktail Sort | O(n) | O(n²) | O(n²) | O(1) |

## Project Structure

```
sorting_visualizer_web/
├── algorithms/
│   ├── __init__.py
│   ├── base.py
│   ├── bubble_sort.py
│   ├── selection_sort.py
│   ├── insertion_sort.py
│   ├── bogo_sort.py
│   ├── comb_sort.py
│   ├── counting_sort.py
│   ├── heap_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   ├── radix_sort.py
│   ├── shell_sort.py
│   ├── tim_sort.py
│   ├── gnome_sort.py
│   └── cocktail_sort.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── templates/
│   └── index.html
├── app.py
└── README.md
```

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sorting_visualizer_web.git
cd sorting_visualizer_web
```

2. Install the required dependencies:
```bash
pip install flask
```

3. Run the application:
```bash
python app.py
```

4. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Select a sorting algorithm from the dropdown menu
2. Adjust the array size using the slider (10-100 elements)
3. Adjust the sorting speed using the speed slider
4. Click "Generate New Array" to create a new random array
5. Click "Start Sorting" to begin the visualization
6. Use "Stop Sorting" to pause the visualization at any time

## Algorithm Descriptions

### Bubble Sort
A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.

### Selection Sort
An in-place comparison sorting algorithm that divides the input list into a sorted and an unsorted region, and repeatedly selects the smallest element from the unsorted region to add to the sorted region.

### Insertion Sort
A simple sorting algorithm that builds the final sorted array one item at a time, by repeatedly inserting a new element into the sorted portion of the array.

### Bogo Sort
A highly inefficient sorting algorithm that generates permutations of the input until it finds one that is sorted.

### Comb Sort
An improvement over bubble sort that uses a gap sequence to eliminate small values at the end of the list.

### Counting Sort
A sorting algorithm that works by counting the number of objects that have distinct key values, then doing some arithmetic to calculate the positions of each key value in the output sequence.

### Heap Sort
A comparison-based sorting algorithm that uses a binary heap data structure to sort elements.

### Merge Sort
A divide-and-conquer algorithm that divides the input array into two halves, recursively sorts the two halves, and then merges the sorted halves.

### Quick Sort
An efficient, in-place sorting algorithm that uses a divide-and-conquer strategy, picking a 'pivot' element and partitioning the array around it.

### Radix Sort
A non-comparative sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value.

### Shell Sort
An optimization of insertion sort that allows the exchange of items that are far apart.

### Tim Sort
A hybrid sorting algorithm derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data.

### Gnome Sort
A sorting algorithm similar to insertion sort, but moving elements to their proper place by a series of swaps.

### Cocktail Sort
A variation of bubble sort that alternately traverses the list in both directions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
