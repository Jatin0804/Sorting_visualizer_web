from .base import BaseSort

class ShellSort(BaseSort):
    def sort(self, arr):
        n = len(arr)
        # Start with a big gap, then reduce the gap
        gap = n // 2

        # Do a gapped insertion sort for this gap size.
        # The first gap elements a[0..gap-1] are already in gapped order
        # keep adding one more element until the entire array is gap sorted
        while gap > 0:
            for i in range(gap, n):
                # add a[i] to the elements that have been gap sorted
                # save a[i] in temp and make a hole at position i
                temp = arr[i]

                # shift earlier gap-sorted elements up until the correct location for a[i] is found
                j = i
                while j >= gap:
                    self.increment_comparisons()
                    if arr[j - gap] > temp:
                        arr[j] = arr[j - gap]
                        self.increment_swaps()
                        self.add_step(arr)
                        j -= gap
                    else:
                        break

                # put temp (the original a[i]) in its correct location
                arr[j] = temp
                self.add_step(arr)

            gap //= 2

        return self.get_stats() 