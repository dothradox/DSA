def linear_search(my_list, target):
    for i, n in enumerate(my_list):
        if n == target:
            print("found")
            return i
    return -1


def binary_search(my_list, left, right, target):
    if right >= left:
        mid = (left + right) // 2
        if my_list[mid] == target:
            return mid
        elif my_list[mid] > target:
            return binary_search(my_list, left, mid - 1, target)
        else:
            return binary_search(my_list, mid + 1, right, target)
    else:
        return -1
