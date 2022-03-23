import random

arr = random.sample(range(10, 300), 50)

small = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[j] < arr[small]:
            small = j
    temp = arr[i]
    arr[i] = arr[small]
    arr[small] = temp

print(arr)
