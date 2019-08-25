def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None
    if number == 0 or number == 1:
        return number
    return sqrt_root(number, 0, number // 2)


def sqrt_root(number, start, end):
    mid = ((start + end) // 2)
    if mid == number // mid:
        return mid
    if mid * mid > number:
        return sqrt_root(number, start, mid - 1)
    else:
        return sqrt_root(number, mid + 1, end)
