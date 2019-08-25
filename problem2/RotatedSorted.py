def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return binary_search(input_list, number, 0, len(input_list) - 1)


def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if mid <= end and array[mid] == target:
        return mid
    if start > end:
        return -1

    if target < array[mid]:
        if array[mid] > array[start] and array[start] <= target:
            return binary_search(array, target, start, mid - 1)
        else:
            return binary_search(array, target, mid + 1, end)
    else:
        if array[mid] < array[end] and array[end] >= target:
            return binary_search(array, target, mid + 1, end)
        else:
            return binary_search(array, target, start, mid - 1)
