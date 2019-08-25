from algorithms.HeapSort import HeapSort


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None or len(input_list) < 2:
        return None
    HeapSort.heap_sort(input_list)
    flag = True
    p1 = ''
    p2 = ''
    for i in range(len(input_list) - 1, -1, -1):
        if flag:
            p1 += str(input_list[i])
        else:
            p2 += str(input_list[i])
        flag = not flag
    return [int(p1), int(p2)]
