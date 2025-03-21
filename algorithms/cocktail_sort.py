from .base import BaseSort

class CocktailSort(BaseSort):
    def sort(self, arr):
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            # Reset the swapped flag on entering the loop
            swapped = False

            # Loop from left to right same as the bubble sort
            for i in range(start, end):
                self.increment_comparisons()
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    self.increment_swaps()
                    self.add_step(arr)
                    swapped = True

            # If nothing moved, then array is sorted
            if not swapped:
                break

            # Otherwise, reset the swapped flag so that it can be used in the next stage
            swapped = False

            # Move the end point back by one, because item at the end is in its rightful spot
            end -= 1

            # From right to left, doing the same comparison as in the previous stage
            for i in range(end - 1, start - 1, -1):
                self.increment_comparisons()
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    self.increment_swaps()
                    self.add_step(arr)
                    swapped = True

            # Increase the starting point, because the last stage would have moved the next smallest number to its rightful spot
            start += 1

        return self.get_stats() 