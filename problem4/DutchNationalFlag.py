def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list is None or len(input_list) < 3:
        return None
    c_l = 0
    left = 0
    right = len(input_list) - 1
    increment = -1
    while left < len(input_list):
        if input_list[left] > input_list[right]:
            tmp = input_list[left]
            input_list[left] = input_list[right]
            input_list[right] = tmp
        if c_l == input_list[left]:
            left += 1
        if left >= right:
            increment = 1
        right += increment
        if right == len(input_list):
            right = len(input_list) - 1
            increment = -1
            c_l += 1
