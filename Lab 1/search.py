def linear_search(my_list, target):
    for i, n in enumerate(my_list):
        if n == target:
            return i
    return -1


def binary_search(my_list, target):
    length = len(my_list)
    low = 0
    high = length - 1
    while high >= low:
        mid = (high + low) // 2
        if my_list[mid] == target:
            return mid
        if my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
