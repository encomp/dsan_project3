

def get_min_max(arr):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       arr(list): list of integers containing one or more integers
    """
    if arr is None or len(arr) < 2:
        return None
    min = arr[0]
    max = arr[0]
    for index in range(1, len(arr)):
        if arr[index] < min:
            min = arr[index]
        if arr[index] > max:
            max = arr[index]
    if min == max:
        return None
    return (min, max)
