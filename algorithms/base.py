class BaseSort:
    def __init__(self):
        self.steps = []
        self.comparisons = 0
        self.swaps = 0
        
        # Time complexity information
        self.complexity = {
            'best': 'O(n)',
            'average': 'O(n)',
            'worst': 'O(n)',
            'space': 'O(1)'
        }

    def sort(self, arr):
        """
        Main sorting method to be implemented by child classes
        """
        raise NotImplementedError("Subclasses must implement sort()")

    def add_step(self, arr):
        """
        Add a step to the visualization
        """
        self.steps.append(arr.copy())

    def increment_comparisons(self):
        """
        Increment the comparison counter
        """
        self.comparisons += 1

    def increment_swaps(self):
        """
        Increment the swap counter
        """
        self.swaps += 1

    def compare(self, a, b):
        self.comparisons += 1
        return a < b

    def swap(self, arr, i, j):
        self.swaps += 1
        arr[i], arr[j] = arr[j], arr[i]

    def get_complexity(self):
        return self.complexity

    def get_stats(self):
        """
        Get sorting statistics
        """
        return {
            'steps': self.steps,
            'comparisons': self.comparisons,
            'swaps': self.swaps,
            'complexity': self.complexity
        } 