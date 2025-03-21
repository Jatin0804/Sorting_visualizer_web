from flask import Flask, render_template, jsonify, request
import random
from algorithms import (
    BubbleSort, SelectionSort, InsertionSort,
    BogoSort, CombSort, CountingSort,
    HeapSort, MergeSort, QuickSort,
    RadixSort, ShellSort, TimSort,
    GnomeSort, CocktailSort
)

app = Flask(__name__)

def generate_array(size=50):
    return [random.randint(10, 500) for _ in range(size)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-array')
def get_array():
    size = request.args.get('size', default=50, type=int)
    return jsonify(generate_array(size))

@app.route('/sort', methods=['POST'])
def sort_array():
    data = request.get_json()
    array = data.get('array', [])
    algorithm = data.get('algorithm', 'bubble')
    
    # Create the appropriate sorting algorithm instance
    sorters = {
        'bubble': BubbleSort,
        'selection': SelectionSort,
        'insertion': InsertionSort,
        'bogo': BogoSort,
        'comb': CombSort,
        'counting': CountingSort,
        'heap': HeapSort,
        'merge': MergeSort,
        'quick': QuickSort,
        'radix': RadixSort,
        'shell': ShellSort,
        'tim': TimSort,
        'gnome': GnomeSort,
        'cocktail': CocktailSort
    }
    
    if algorithm not in sorters:
        return jsonify({'error': 'Invalid algorithm'}), 400
    
    # Sort the array and get the results
    sorter = sorters[algorithm]()
    result = sorter.sort(array.copy())
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True) 