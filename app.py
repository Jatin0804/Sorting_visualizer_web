from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import random
from algorithms import (
    BubbleSort, SelectionSort, InsertionSort,
    BogoSort, CombSort, CountingSort,
    HeapSort, MergeSort, QuickSort,
    RadixSort, ShellSort, TimSort,
    GnomeSort, CocktailSort
)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Create instances of all sorting algorithms
sorting_algorithms = {
    'bubble': BubbleSort(),
    'selection': SelectionSort(),
    'insertion': InsertionSort(),
    'bogo': BogoSort(),
    'comb': CombSort(),
    'counting': CountingSort(),
    'heap': HeapSort(),
    'merge': MergeSort(),
    'quick': QuickSort(),
    'radix': RadixSort(),
    'shell': ShellSort(),
    'tim': TimSort(),
    'gnome': GnomeSort(),
    'cocktail': CocktailSort()
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate-array')
def generate_array():
    size = int(request.args.get('size', 50))
    array = [random.randint(1, 500) for _ in range(size)]
    return jsonify(array)

@app.route('/api/sort', methods=['POST'])
def sort():
    data = request.get_json()
    array = data.get('array', [])
    algorithm = data.get('algorithm', 'bubble')
    
    if algorithm not in sorting_algorithms:
        return jsonify({'error': 'Invalid algorithm'}), 400
    
    sorter = sorting_algorithms[algorithm]
    result = sorter.sort(array.copy())
    return jsonify(result)

@app.route('/api/complexities')
def get_complexities():
    complexities = {
        name: algorithm.get_complexity()
        for name, algorithm in sorting_algorithms.items()
    }
    return jsonify(complexities)

if __name__ == '__main__':
    app.run(debug=True) 