class BaseSort:
    def __init__(self):
        self.steps = []
        self.comparisons = 0
        self.swaps = 0

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

    def get_stats(self):
        """
        Get sorting statistics
        """
        return {
            'steps': self.steps,
            'comparisons': self.comparisons,
            'swaps': self.swaps
        } 