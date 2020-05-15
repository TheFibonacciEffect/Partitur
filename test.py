
# There are different ways to do a Quick Sort partition, this implements the
# Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.
def partition(y, x, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = y[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while y[i] < pivot:
            i += 1

        j -= 1
        while y[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        y[i], y[j] = y[j], y[i]
        x[i], x[j] = x[j], x[i]


def quick_sort(y,x):
    # Create a helper function that will be called recursively
    def _quick_sort(y, x, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(y,x, low, high)
            _quick_sort(y,x, low, split_index)
            _quick_sort(y,x, split_index + 1, high)

    _quick_sort(y,x, 0, len(y) - 1)

y = [1,5,2,8]

x = list(range(len(y)))

quick_sort(y,x)

print(x,y)

