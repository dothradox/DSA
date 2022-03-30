def insertion_sort(arr):
    # Our index starts from 0
    for i in range(1, len(arr)):
        # Key is the second element in the list
        key = arr[i]

        # j denotes the index of the first element in the list
        j = i - 1

        # Decrement j until key is smaller than the value
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr
