def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right, arr)


def merge(l, r, arr):
    i = j = 0
    while i + j < len(arr):
        # if j is already incremented to last index of right fill all remaining to left
        if j == len(r) or (i < len(l) and l[i] < r[j]):
            arr[i + j] = l[i]
            i += 1
        else:
            arr[i + j] = r[j]
            j += 1


my_list = [2, 3, 6, 2, 6, 8, 93, 2, 3, 5, 6]
print(merge_sort(my_list))
