def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        # i for left half and j for right half
        i = 0
        j = 0

        k = 0

        # Loop until either of the half has been sorted into position
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # reamining elements are all in right or left half
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(arr)
print(arr)